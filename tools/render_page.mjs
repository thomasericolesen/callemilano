#!/usr/bin/env node
// Render one page in headless Chromium (Playwright) and print JSON to stdout:
//   {"url", "final_url", "http", "text", "menu_links": [{"text", "href"}], "error"}
// Used by `tools/intake.py fetch` as the free second step after curl and before Tavily,
// for pages that need JavaScript (Wix, React and similar). No cookies, logins or stealth:
// pages that block bots stay blocked and fall through to the next step.
// Usage: node tools/render_page.mjs URL [timeout_ms]
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
let chromium;
try {
  ({ chromium } = require("playwright"));
} catch {
  console.log(JSON.stringify({ error: "playwright_not_installed" }));
  process.exit(0);
}

const url = process.argv[2];
const timeout = Number(process.argv[3] || 30000);
const out = { url, final_url: null, http: null, text: "", menu_links: [], error: null };
let browser;
try {
  browser = await chromium.launch(
    process.env.PW_CHROMIUM ? { executablePath: process.env.PW_CHROMIUM } : {},
  );
  const page = await browser.newPage({
    userAgent: "Mozilla/5.0 (CalleMilano fact check; headless Chromium)",
    locale: "es-ES",
  });
  const resp = await page.goto(url, { waitUntil: "domcontentloaded", timeout });
  out.http = resp ? resp.status() : null;
  // Give client-side rendering a moment; ignore pages that never go quiet.
  await page.waitForLoadState("networkidle", { timeout: Math.min(timeout, 15000) }).catch(() => {});
  out.final_url = page.url();
  out.text = (await page.locator("body").innerText({ timeout: 5000 }).catch(() => "")) || "";
  out.menu_links = await page.$$eval("a[href]", (as) =>
    as
      .map((a) => ({ text: (a.innerText || "").trim().slice(0, 80), href: a.href }))
      .filter((l) => /menu|men[uú]|carta|card|\.pdf/i.test(l.text + " " + l.href))
      .slice(0, 20),
  );
} catch (e) {
  out.error = String(e && e.message ? e.message.split("\n")[0] : e);
} finally {
  if (browser) await browser.close();
}
console.log(JSON.stringify(out));
