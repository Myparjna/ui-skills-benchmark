import asyncio
import os
from playwright.async_api import async_playwright

EXHIBITION_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR = os.path.join(EXHIBITION_DIR, 'assets', 'screenshots')
SERVER_URL = 'http://127.0.0.1:8080'

skills = [
    'web-design-guidelines', 'frontend-design', 'stitch-design', 'ui-ux-pro-max',
    'frontend-design-pro', 'design-taste-frontend', 'modern-frontend-design',
    'nuxt-ui', 'sleek-design-mobile-apps', 'shadcn', 'impeccable',
    'taste-skill', 'modern-web-design', 'superdesign'
]
scenarios = ['airline', 'charging', 'bikeops']

files = []
for s in skills:
    for sc in scenarios:
        files.append(f'qwen3.7-plus-{s}-{sc}.html')

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

async def screenshot_page(browser, filename):
    is_mobile = 'charging' in filename
    url = f'{SERVER_URL}/pages/{filename}'
    out_path = os.path.join(SCREENSHOTS_DIR, filename.replace('.html', '.png'))

    if is_mobile:
        context_kwargs = {'viewport': {'width': 390, 'height': 844}, 'device_scale_factor': 2}
    else:
        # 16:9 桌面端
        context_kwargs = {'viewport': {'width': 1280, 'height': 720}}

    context = await browser.new_context(**context_kwargs)
    page = await context.new_page()
    try:
        await page.goto(url, wait_until='domcontentloaded', timeout=15000)
        await page.wait_for_timeout(1000)
        await page.screenshot(path=out_path)
        print(f'  OK  {filename}')
    except Exception as e:
        print(f'  ERR {filename}: {e}')
    finally:
        await context.close()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        total = len(files)
        print(f'共 {total} 个页面需要截图...')
        for i, f in enumerate(files, 1):
            print(f'[{i}/{total}] ', end='')
            await screenshot_page(browser, f)
        await browser.close()
        print('完成！')

asyncio.run(main())
