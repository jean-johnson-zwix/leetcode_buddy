const https = require("https");

function post(hostname, path, headers, body) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(body);
    const req = https.request(
      { hostname, path, method: "POST", headers: { ...headers, "Content-Length": Buffer.byteLength(data) } },
      (res) => {
        let raw = "";
        res.on("data", (c) => (raw += c));
        res.on("end", () => {
          try { resolve({ status: res.statusCode, body: JSON.parse(raw) }); }
          catch { resolve({ status: res.statusCode, body: raw }); }
        });
      }
    );
    req.on("error", reject);
    req.write(data);
    req.end();
  });
}

function get(hostname, path, headers) {
  return new Promise((resolve, reject) => {
    const req = https.request(
      { hostname, path, method: "GET", headers },
      (res) => {
        let raw = "";
        res.on("data", (c) => (raw += c));
        res.on("end", () => {
          try { resolve({ status: res.statusCode, body: JSON.parse(raw) }); }
          catch { resolve({ status: res.statusCode, body: raw }); }
        });
      }
    );
    req.on("error", reject);
    req.end();
  });
}

function put(hostname, path, headers, body) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(body);
    const req = https.request(
      { hostname, path, method: "PUT", headers: { ...headers, "Content-Length": Buffer.byteLength(data) } },
      (res) => {
        let raw = "";
        res.on("data", (c) => (raw += c));
        res.on("end", () => {
          try { resolve({ status: res.statusCode, body: JSON.parse(raw) }); }
          catch { resolve({ status: res.statusCode, body: raw }); }
        });
      }
    );
    req.on("error", reject);
    req.write(data);
    req.end();
  });
}

exports.handler = async (event) => {
  const CORS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
  };

  if (event.httpMethod === "OPTIONS") return { statusCode: 200, headers: CORS, body: "" };
  if (event.httpMethod !== "POST") return { statusCode: 405, headers: CORS, body: "Method Not Allowed" };

  const GEMINI_KEY    = process.env.GEMINI_API_KEY;
  const GITHUB_TOKEN  = process.env.GITHUB_TOKEN;
  const GITHUB_OWNER  = process.env.GITHUB_OWNER;
  const GITHUB_REPO   = process.env.GITHUB_REPO || "leetcode_buddy";

  if (!GEMINI_KEY || !GITHUB_TOKEN || !GITHUB_OWNER) {
    return { statusCode: 500, headers: CORS, body: JSON.stringify({ error: "Missing environment variables." }) };
  }

  let payload;
  try { payload = JSON.parse(event.body); }
  catch { return { statusCode: 400, headers: CORS, body: JSON.stringify({ error: "Invalid JSON body." }) }; }

  const { leetcodeUrl, solution, insight, stars } = payload;
  if (!leetcodeUrl || !solution || !insight || !stars) {
    return { statusCode: 400, headers: CORS, body: JSON.stringify({ error: "Missing required fields." }) };
  }

  // ── 1. Ask Gemini to enrich the solution ──
  const prompt = `You are a LeetCode expert. Analyze the following and respond ONLY with a valid JSON object — no markdown, no explanation, no backticks.

LeetCode URL: ${leetcodeUrl}
Solution (Python): 
${solution}

User's insight: ${insight}
User's self-rating: ${stars}/5 stars

Return this exact JSON structure:
{
  "problem_name": "Human readable problem name",
  "problem_number": "LC number as string e.g. 1",
  "difficulty": "Easy | Medium | Hard",
  "folder": "one of: arrays | strings | hashmaps | two_pointers | sliding_window | binary_search | linked_lists | stacks_queues | intervals | trees | graphs | backtracking | heaps | tries | dynamic_programming | greedy | advanced_graphs | bit_manipulation | math | other",
  "pattern": "Primary pattern name e.g. HashMap, Two Pointer, Sliding Window, BFS, DFS, DP - 1D, DP - 2D, Backtracking, Binary Search, Monotonic Stack, Union Find, Trie, Heap, Greedy",
  "approach": "2-3 sentence explanation of the approach used",
  "time_complexity": "e.g. O(n)",
  "space_complexity": "e.g. O(n)",
  "key_insight": "The single most important thing to remember about this problem",
  "gotchas": "Common mistakes or edge cases to watch out for",
  "revisit": true or false (true if stars <= 3),
  "stars": ${stars},
  "date": "${new Date().toISOString().split("T")[0]}",
  "patterns_md_entry": "One concise line for patterns.md e.g.: | Two Sum (#1) | HashMap | Store value→index; look up complement | O(n) | O(n) | ⭐⭐⭐⭐⭐ |"
}`;

  const geminiRes = await post(
    "generativelanguage.googleapis.com",
    `/v1beta/models/gemini-2.5-flash:generateContent?key=${GEMINI_KEY}`,
    { "Content-Type": "application/json" },
    {
      contents: [{ parts: [{ text: prompt }] }],
      generationConfig: { temperature: 0 },
    }
  );

  if (geminiRes.status !== 200) {
    return { statusCode: 502, headers: CORS, body: JSON.stringify({ error: "Gemini API failed.", detail: geminiRes.body }) };
  }

  let meta;
  try {
    let raw = geminiRes.body.candidates[0].content.parts[0].text.trim();
    // Strip markdown code fences if Gemini adds them anyway
    raw = raw.replace(/^```json\s*/i, "").replace(/^```\s*/i, "").replace(/```\s*$/i, "").trim();
    meta = JSON.parse(raw);
  } catch {
    return { statusCode: 502, headers: CORS, body: JSON.stringify({ error: "Failed to parse Gemini response.", detail: geminiRes.body }) };
  }

  // ── 2. Build the enriched solution file ──
  const starStr = "⭐".repeat(meta.stars) + "☆".repeat(5 - meta.stars);
  const revisitFlag = meta.revisit ? "🔁 YES — add to revision list" : "✅ No";

  const fileContent =
`# ${meta.problem_name} (LC #${meta.problem_number})
# URL: ${leetcodeUrl}
# ─────────────────────────────────────────
# DIFFICULTY : ${meta.difficulty}
# PATTERN    : ${meta.pattern}
# APPROACH   : ${meta.approach}
# TIME       : ${meta.time_complexity}
# SPACE      : ${meta.space_complexity}
# ─────────────────────────────────────────
# KEY INSIGHT: ${meta.key_insight}
# GOTCHAS    : ${meta.gotchas}
# ─────────────────────────────────────────
# RATING     : ${starStr} (${meta.stars}/5)
# REVISIT    : ${revisitFlag}
# DATE       : ${meta.date}
# ─────────────────────────────────────────
# YOUR INSIGHT:
# ${insight.split("\n").join("\n# ")}

${solution}
`;

  // ── 3. Commit solution file to GitHub ──
  const safeName = meta.problem_name.toLowerCase().replace(/[^a-z0-9]+/g, "_");
  const filePath = `solutions/${meta.folder}/${safeName}.py`;
  const ghHeaders = {
    "Content-Type": "application/json",
    Authorization: `token ${GITHUB_TOKEN}`,
    "User-Agent": "leetcode-tracker-bot",
  };

  // Check if file exists (to get sha for update)
  const existing = await get("api.github.com", `/repos/${GITHUB_OWNER}/${GITHUB_REPO}/contents/${filePath}`, ghHeaders);
  const fileSha = existing.status === 200 ? existing.body.sha : undefined;

  const filePayload = {
    message: `leetcode buddy: add solution: ${meta.problem_name} (LC #${meta.problem_number}) ${starStr}`,
    content: Buffer.from(fileContent).toString("base64"),
    ...(fileSha ? { sha: fileSha } : {}),
  };

  const fileRes = await put("api.github.com", `/repos/${GITHUB_OWNER}/${GITHUB_REPO}/contents/${filePath}`, ghHeaders, filePayload);

  if (fileRes.status !== 200 && fileRes.status !== 201) {
    return { statusCode: 502, headers: CORS, body: JSON.stringify({ error: "GitHub file commit failed.", detail: fileRes.body }) };
  }

  // ── 4. Update patterns.md ──
  const patternsPath = "notes/patterns.md";
  const patternsExisting = await get("api.github.com", `/repos/${GITHUB_OWNER}/${GITHUB_REPO}/contents/${patternsPath}`, ghHeaders);

  let currentContent = "";
  let patternsSha;

  if (patternsExisting.status === 200) {
    currentContent = Buffer.from(patternsExisting.body.content, "base64").toString("utf8");
    patternsSha = patternsExisting.body.sha;
  } else {
    currentContent = `# Pattern Reference\n\nA running log of every problem solved, organized by pattern.\n\n| Problem | Pattern | Key Insight | Time | Space | Rating |\n|---------|---------|-------------|------|-------|--------|\n`;
  }

  const newContent = currentContent.trimEnd() + "\n" + meta.patterns_md_entry + "\n";

  const patternsPayload = {
    message: `leetcode buddy: update patterns.md: ${meta.problem_name}`,
    content: Buffer.from(newContent).toString("base64"),
    ...(patternsSha ? { sha: patternsSha } : {}),
  };

  await put("api.github.com", `/repos/${GITHUB_OWNER}/${GITHUB_REPO}/contents/${patternsPath}`, ghHeaders, patternsPayload);

  // ── 5. Return success ──
  return {
    statusCode: 200,
    headers: CORS,
    body: JSON.stringify({
      success: true,
      problem_name: meta.problem_name,
      problem_number: meta.problem_number,
      difficulty: meta.difficulty,
      pattern: meta.pattern,
      folder: meta.folder,
      time_complexity: meta.time_complexity,
      space_complexity: meta.space_complexity,
      approach: meta.approach,
      key_insight: meta.key_insight,
      gotchas: meta.gotchas,
      revisit: meta.revisit,
      stars: meta.stars,
      file_path: filePath,
    }),
  };
};