from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://yugenanime.tv/")
    page.wait_for_selector('a:has-text("Sign in")')
    page.get_by_text("Sign in", exact=True).click()
    page.get_by_placeholder("Email").fill("predatorakki0906@gmail.com")
    page.get_by_placeholder("Password").fill("pr$_p-YzVKq5$-t")
    page.get_by_role("button", name="Sign in").click()
    page.screenshot(path="example.png")
    browser.close()
