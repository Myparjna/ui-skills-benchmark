import asyncio
import os
from playwright.async_api import async_playwright

EXHIBITION_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR = os.path.join(EXHIBITION_DIR, 'assets', 'screenshots')
SERVER_URL = 'http://127.0.0.1:8766'

# Mimo V2.5 小程序文件列表
MIMO_V25_CHARGING_FILES = [
    'mimoV25-design-taste-frontend-ev-charging.html',
    'mimoV25-frontend-design-ev-charging.html',
    'mimoV25-frontend-design-pro-ev-charging.html',
    'mimoV25-impeccable-ev-charging.html',
    'mimoV25-modern-frontend-design-ev-charging.html',
    'mimoV25-modern-web-design-ev-charging.html',
    'mimoV25-nuxt-ui-ev-charging.html',
    'mimoV25-shadcn-ev-charging.html',
    'mimoV25-sleek-design-mobile-apps-ev-charging.html',
    'mimoV25-stitch-design-ev-charging.html',
    'mimoV25-superdesign-ev-charging.html',
    'mimoV25-taste-skill-ev-charging.html',
    'mimoV25-ui-ux-pro-max-ev-charging.html',
    'mimoV25-web-design-guidelines-ev-charging.html',
]

async def screenshot_mobile_page(browser, filename):
    """截取移动端页面，只截取手机屏幕部分（9:16比例）"""
    url = f'{SERVER_URL}/pages/{filename}'
    out_path = os.path.join(SCREENSHOTS_DIR, filename.replace('.html', '.png'))

    # 使用9:16比例的视口
    # 标准iPhone屏幕：390x844（约9:16比例）
    # 不使用device_scale_factor，确保截图比例正确
    context = await browser.new_context(
        viewport={'width': 390, 'height': 844},
        device_scale_factor=1
    )
    page = await context.new_page()
    try:
        await page.goto(url, wait_until='networkidle', timeout=60000)
        await asyncio.sleep(2)
        
        # 隐藏滚动条，确保只截取视口内容
        await page.evaluate('''() => {
            document.body.style.overflow = 'hidden';
            document.documentElement.style.overflow = 'hidden';
        }''')
        
        # 截取视口内容（不滚动），只截取手机屏幕部分
        await page.screenshot(path=out_path, full_page=False, type='png')
        
        print(f'OK: {filename}')
    except Exception as e:
        print(f'FAIL: {filename} - {e}')
    finally:
        await context.close()

async def main():
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for i, filename in enumerate(MIMO_V25_CHARGING_FILES):
            print(f'[{i+1}/{len(MIMO_V25_CHARGING_FILES)}] {filename}')
            await screenshot_mobile_page(browser, filename)
        await browser.close()
    print('All Mimo V2.5 charging screenshots done!')

if __name__ == '__main__':
    asyncio.run(main())