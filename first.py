from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False,slow_mo=3000)
    browser1=p.firefox.launch(headless=False,slow_mo=3000)
    #creates new tab in the browser
    page=browser.new_page()
    url="https://saucedemo.com/"
    page.goto(url)
    # page.go_back()
    # page.go_forward()
    # #referesh the page
    # page.reload()
    page1=browser1.new_page()
    page1.goto("https://www.google.com/")
    print(page1.title())
    print(page1.url)
    page1.screenshot(path="screenshot.png")
    browser.close()
    browser1.close()


    #device ko herera aaunu 
