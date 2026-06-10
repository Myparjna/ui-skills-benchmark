const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');
const http = require('http');

const EXHIBITION_DIR = path.resolve(__dirname);
const PAGES_DIR = path.join(EXHIBITION_DIR, 'pages');
const SCREENSHOTS_DIR = path.join(EXHIBITION_DIR, 'assets', 'screenshots');

const files = [
  'kimi-k2.6-design-taste-frontend-airline.html',
  'kimi-k2.6-design-taste-frontend-bikeops.html',
  'kimi-k2.6-design-taste-frontend-charging.html',
  'kimi-k2.6-frontend-design-airline.html',
  'kimi-k2.6-frontend-design-bikeops.html',
  'kimi-k2.6-frontend-design-charging.html',
  'kimi-k2.6-frontend-design-pro-airline.html',
  'kimi-k2.6-frontend-design-pro-bikeops.html',
  'kimi-k2.6-frontend-design-pro-charging.html',
  'kimi-k2.6-impeccable-airline.html',
  'kimi-k2.6-impeccable-bikeops.html',
  'kimi-k2.6-impeccable-charging.html',
  'kimi-k2.6-modern-frontend-design-airline.html',
  'kimi-k2.6-modern-frontend-design-bikeops.html',
  'kimi-k2.6-modern-frontend-design-charging.html',
  'kimi-k2.6-modern-web-design-airline.html',
  'kimi-k2.6-modern-web-design-bikeops.html',
  'kimi-k2.6-modern-web-design-charging.html',
  'kimi-k2.6-nuxt-ui-airline.html',
  'kimi-k2.6-nuxt-ui-bikeops.html',
  'kimi-k2.6-nuxt-ui-charging.html',
  'kimi-k2.6-shadcn-airline.html',
  'kimi-k2.6-shadcn-bikeops.html',
  'kimi-k2.6-shadcn-charging.html',
  'kimi-k2.6-sleek-design-mobile-apps-airline.html',
  'kimi-k2.6-sleek-design-mobile-apps-bikeops.html',
  'kimi-k2.6-sleek-design-mobile-apps-charging.html',
  'kimi-k2.6-stitch-design-airline.html',
  'kimi-k2.6-stitch-design-bikeops.html',
  'kimi-k2.6-stitch-design-charging.html',
  'kimi-k2.6-superdesign-airline.html',
  'kimi-k2.6-superdesign-bikeops.html',
  'kimi-k2.6-superdesign-charging.html',
  'kimi-k2.6-taste-skill-airline.html',
  'kimi-k2.6-taste-skill-bikeops.html',
  'kimi-k2.6-taste-skill-charging.html',
  'kimi-k2.6-ui-ux-pro-max-airline.html',
  'kimi-k2.6-ui-ux-pro-max-bikeops.html',
  'kimi-k2.6-ui-ux-pro-max-charging.html',
  'kimi-k2.6-web-design-guidelines-airline.html',
  'kimi-k2.6-web-design-guidelines-bikeops.html',
  'kimi-k2.6-web-design-guidelines-charging.html',
];

async function startServer() {
  const server = http.createServer((req, res) => {
    const url = new URL(req.url, `http://localhost`);
    let filePath = path.join(EXHIBITION_DIR, decodeURIComponent(url.pathname));
    if (url.pathname === '/') filePath = path.join(EXHIBITION_DIR, 'index.html');

    fs.readFile(filePath, (err, data) => {
      if (err) {
        res.writeHead(404); res.end('Not found'); return;
      }
      const ext = path.extname(filePath);
      const mime = {
        '.html': 'text/html', '.js': 'application/javascript',
        '.css': 'text/css', '.png': 'image/png', '.jpg': 'image/jpeg',
        '.svg': 'image/svg+xml', '.json': 'application/json'
      }[ext] || 'application/octet-stream';
      res.writeHead(200, { 'Content-Type': mime, 'Access-Control-Allow-Origin': '*' });
      res.end(data);
    });
  });
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const port = server.address().port;
  console.log(`Server running on http://127.0.0.1:${port}`);
  return { server, port };
}

async function screenshot(browser, port, filename) {
  const page = await browser.newPage();
  const isMobile = filename.includes('charging');
  const url = `http://127.0.0.1:${port}/pages/${filename}`;

  if (isMobile) {
    await page.setViewport({ width: 414, height: 896, deviceScaleFactor: 2 });
  } else {
    await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  }

  try {
    await page.goto(url, { waitUntil: 'networkidle0', timeout: 60000 });
    await new Promise(r => setTimeout(r, 2000));

    const outFile = path.join(SCREENSHOTS_DIR, filename.replace('.html', '.png'));
    await page.screenshot({
      path: outFile,
      fullPage: false,
      type: 'png'
    });
    console.log(`OK: ${filename} -> ${outFile}`);
  } catch (e) {
    console.error(`FAIL: ${filename} - ${e.message}`);
  } finally {
    await page.close();
  }
}

(async () => {
  if (!fs.existsSync(SCREENSHOTS_DIR)) fs.mkdirSync(SCREENSHOTS_DIR, { recursive: true });

  const { server, port } = await startServer();
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox', '--disable-setuid-sandbox'] });

  for (let i = 0; i < files.length; i++) {
    console.log(`[${i + 1}/${files.length}] ${files[i]}`);
    await screenshot(browser, port, files[i]);
  }

  await browser.close();
  server.close();
  console.log('All screenshots done!');
})();
