# In pycharm console, type playwright codegen
# code will be generated while navigating site


import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    # can set default timeout for all actions
    page.set_default_timeout(3000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    #page.pause()
    # page.wait_for_load_state("networkidle") # find alternative to netowrkidle
    #page.wait_for_timeout(500)              # works but should find alternative. only good for debug mode
    page.wait_for_timeout(500)
    page.get_by_test_id("handle-button").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()

    # alternative examples (might be old):
    # page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("symon.storozhenko@gmail.com")
    # page.fill("[data-testid='siteMembers.container'] input[type='email']", "symon.storozhenko@gmail.com")
    page.fill('input:below(:text("Email"))', "symon.storozhenko@gmail.com")
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("symon.storozhenko@gmail.com")
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("Tab")
    page.get_by_role("textbox", name="Password").fill("test123")
    page.get_by_role("textbox", name="Password").press("Enter")
    expect(page.get_by_role("button", name="Log in with Email")).to_be_hidden()

    print("pass")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
