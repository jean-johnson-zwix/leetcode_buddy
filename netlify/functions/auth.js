exports.handler = async (event) => {
  const CORS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
  };
  if (event.httpMethod === "OPTIONS") return { statusCode: 200, headers: CORS, body: "" };
  if (event.httpMethod !== "POST") return { statusCode: 405, headers: CORS, body: "Method Not Allowed" };

const CORRECT_PASSWORD = process.env.SUBMIT_PASSWORD;
console.log('ENV PASSWORD:', JSON.stringify(CORRECT_PASSWORD));
  console.log('BODY PASSWORD:', JSON.stringify(body.password));
  if (!CORRECT_PASSWORD) {
    return { statusCode: 500, headers: CORS, body: JSON.stringify({ ok: false, error: "SUBMIT_PASSWORD env var not set." }) };
  }

  let body;
  try { body = JSON.parse(event.body); }
  catch { return { statusCode: 400, headers: CORS, body: JSON.stringify({ ok: false }) }; }

  const ok = body.password === CORRECT_PASSWORD;
  return {
    statusCode: 200,
    headers: CORS,
    body: JSON.stringify({ ok }),
  };
};
