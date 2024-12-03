import re
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from POM.Rullete import Rullete
def test_Place_Bet():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        obje_rullete = Rullete(page)
        obje_rullete.navigate()



