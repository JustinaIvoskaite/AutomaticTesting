import re
import time

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
    #page.get_by_placeholder("Enter Password").press("Enter")
    page.get_by_role("button", name="Log in").click()
    #page.locator(".category-block").first.click()
    #time.sleep(15)
    page.get_by_role("link", name='Roulettes').click()
    balance_val = float(page.locator("#username-comp-cash-amount").text_content().replace("€", "").replace(",", ""))
    print(balance_val)
    page.get_by_role("button", name="1 6").click()
    #select different:
    page.locator("#roulette-chip-10").click()
    page.get_by_role("button", name="15").click()
    page.get_by_text("Place a bet").click()
    time.sleep(30)
    expect(page.get_by_text("Place a bet")).to_be_enabled()

    # ---------------------
    context.close()
    browser.close()

def run2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://qa-test.online.advbet.com/sports/football")
    page.get_by_text("Login").click()
    page.get_by_placeholder("Enter email or mobile number").click()
    page.get_by_placeholder("Enter email or mobile number").fill("gw0@adv.bet")
    page.get_by_placeholder("Enter email or mobile number").press("Tab")
    page.get_by_placeholder("Enter Password").fill("qatest123+")
    page.get_by_role("button", name="Log in").click()
    page.get_by_role("link", name='Roulettes').click()
    page.get_by_role("button", name="1 6").click()

    page.locator(".button").first.click()




with sync_playwright() as playwright:
    run(playwright)
    run2(playwright)

