import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://qa-test.online.advbet.com/sports/football")
    page.get_by_text("Login").click()
    page.get_by_placeholder("Enter email or mobile number").click()
    page.get_by_placeholder("Enter email or mobile number").fill("gw0@adv.bet")
    page.get_by_placeholder("Enter email or mobile number").press("Tab")
    page.get_by_placeholder("Enter Password").fill("qatest123+")
    page.get_by_placeholder("Enter Password").press("Enter")
    page.get_by_role("button", name="Log in").click()
    page.locator(".category-block").first.click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
