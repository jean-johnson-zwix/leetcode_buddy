# LeetCode Tracker

An AI-powered LeetCode Buddy that trackes your progress and solutions and takes you from Zero to Master!

## What It Does

Submit a LeetCode solution from the web app and the system automatically:

- Calls **Gemini 2.5 Flash** to analyze your code and generate structured metadata (pattern, approach, time/space complexity, key insight, gotchas, revisit flag)
- Commits the enriched `.py` file to the correct topic folder in this repo (`solutions/arrays/`, `solutions/trees/`, etc.)
- Appends a row to `notes/patterns.md` — a running log of every problem solved by pattern

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML/CSS/JS |
| Hosting | Netlify (free tier) |
| Serverless Functions | Netlify Functions (Node.js) |
| AI Enrichment | Google Gemini API |
| Solution Storage | GitHub API (direct commit via REST) |
| Email | EmailJS |

## Setup

### Prerequisites
- A [Netlify](https://netlify.com) account (free)
- A [Google AI Studio](https://aistudio.google.com/app/apikey) API key (free, 1,500 req/day)
- A GitHub personal access token with **Contents: Read & Write** on this repo

### Environment Variables

Set these in **Netlify → Site → Environment Variables**:

| Key | Description | Secret? |
|---|---|---|
| `GEMINI_API_KEY` | Google AI Studio API key |
| `GITHUB_TOKEN` | Fine-grained personal access token |
| `GITHUB_OWNER` | Your GitHub username |
| `GITHUB_REPO` | This repo name (`leetcode_buddy`) |
| `SUBMIT_PASSWORD` | Password to unlock the submit tab |

### Deploy

1. Fork or clone this repo
2. Connect to Netlify via **Add new site → Import from Git**
3. Add the environment variables above
4. Trigger a deploy — Netlify auto-deploys on every push