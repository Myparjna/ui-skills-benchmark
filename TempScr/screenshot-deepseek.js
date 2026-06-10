const { chromium } = require('playwright');
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = 'C:\\Users\\mypra\\Desktop\\VibeCoding指南\\skills测评项目\\01-前端设计技能测评';
const HTML_DIR = path.join(ROOT, '03-产出', 'deepseek');
const SCREENSHOT_DIR = path.join(ROOT, 'ScreenShot', 'deepseek');
const PORT = 18924;

// Ensure screenshot dir
if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

// Simple HTTP server to serve the HTML directory
const server = http.createServer((req, res) => {
  // Security: only serve our specific directory
  const safePath = path.normalize(path.join(HTML_DIR, req.url === '/' ? 'deepseek-no-skill-airline.html' : req.url));
  if (!safePath.startsWith(HTML_DIR)) {
    res.writeHead(403);
    res.end('Forbidden');
    return;
  }
  const ext = path.extname(safePath).toLowerCase();
  const mime = {
    '.html': 'text/html; charset=utf-8',
    '.htm': 'text/html; charset=utf-8',
  };
  fs.readFile(safePath, (err, data) => {
    if (err) { res.writeHead(404); res.end('Not found'); return; }
    res.writeHead(200, { 'Content-Type': mime[ext] || 'text/plain' });
    res.end(data);
  });
});

(async () => {
  // Start server
  await new Promise(resolve => server.listen(PORT, '127.0.0.1', resolve));
  console.log(`Server on http://127.0.0.1:${PORT}`);

  const browser = await chromium.launch({
    headless: true,
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
  });

  // Get all HTML files
  const files = fs.readdirSync(HTML_DIR).filter(f => f.endsWith('.html')).sort();

  console.log(`Total files to screenshot: ${files.length}`);

  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
  });

  let ok = 0, fail = 0;

  for (const file of files) {
    const screenshotName = file.replace('.html', '.png');
    const screenshotPath = path.join(SCREENSHOT_DIR, screenshotName);
    const url = `http://127.0.0.1:${PORT}/${encodeURIComponent(file)}`;

    try {
      const page = await context.newPage();
      await page.goto(url, { waitUntil: 'networkidle0', timeout: 30000 });
      await page.waitForTimeout(1500); // let animations finish
      await page.screenshot({ path: screenshotPath, fullPage: false });
      await page.close();
      ok++;
      process.stdout.write(`+`);
    } catch (e) {
      fail++;
      process.stdout.write(`x`);
    }
  }

  await browser.close();
  server.close();

  console.log(`\nDone: ${ok} OK, ${fail} Failed`);
})();