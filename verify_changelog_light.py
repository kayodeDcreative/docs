from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(color_scheme="light")
    page = context.new_page()
    page.goto("http://localhost:3000/changelog")
    page.screenshot(path="verification-light.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
