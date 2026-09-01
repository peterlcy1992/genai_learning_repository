// Render the poster HTML files in build/ to 3000x3000 PNGs in png/.
// Requires Playwright + a Chromium build. On Claude Code on the web the
// pre-installed Chromium lives under $PLAYWRIGHT_BROWSERS_PATH; elsewhere run
// `npx playwright install chromium` first. Override the binary with
// CHROMIUM_PATH=/path/to/chrome if Playwright can't find one automatically.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// BUILD_DIR / OUT_DIR override the defaults so the same renderer serves both
// the stage thumbnails (build/ -> png/) and per-episode podcast covers
// (podcast_build/ -> ../../docs/thumbnails/podcast/). Values are resolved
// relative to this file.
const BUILD = path.resolve(__dirname, process.env.BUILD_DIR || 'build');
const OUT = path.resolve(__dirname, process.env.OUT_DIR || 'png');
fs.mkdirSync(OUT, { recursive: true });

(async () => {
  const launch = { args: ['--no-sandbox', '--force-color-profile=srgb'] };
  if (process.env.CHROMIUM_PATH) launch.executablePath = process.env.CHROMIUM_PATH;
  const browser = await chromium.launch(launch);
  const page = await browser.newPage({
    viewport: { width: 3000, height: 3000 },
    deviceScaleFactor: 1,
  });
  const files = fs.readdirSync(BUILD).filter((f) => f.endsWith('.html')).sort();
  for (const f of files) {
    const slug = f.replace('.html', '');
    await page.goto('file://' + path.join(BUILD, f));
    await page.evaluate(() => document.fonts.ready);
    const svg = await page.$('svg');
    await svg.screenshot({ path: path.join(OUT, slug + '.png') });
    console.log('rendered', slug);
  }
  await browser.close();
})();
