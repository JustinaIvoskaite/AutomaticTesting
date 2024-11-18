import asyncio
import helpers
import pytest
from playwright.async_api import Page, expect, async_playwright
from pageObjects.PlaceTheBet import PlaceTheBet
from pageObjects.ContactService import ContactTheService



def ContactingServiceTest(page: Page):
    page.goto("https://demo.betgames.tv")
    language_first = "Lithuanian"
    language_second = "English"
    get_language_parent  = page.locator("#language")
    #selected = get_language_parent.locator("a").text_content().strip()

    email_input = await page.locator("#email")
    message_input =await page.locator("#message")
    send_btn  =await page.locator(".send.btn.btn-primary.pull-left")

    email_input.fill("kazkas@gmail.com")
    message_input.fill("Testavimo zinute")
    should_be = helpers.GetMessageByLanguage(language_second)
    await send_btn.click()
    # message for success if sent
    success = await page.locator("#send")
    got_text = await success.text_content()
    print(f"Text received: '{got_text}'")
    assert got_text == should_be, f"Message is not correct. Expected: '{should_be}', Found: '{got_text}'"

if __name__ == "__main__":
    #Verification()
    #ContactingServiceTest()
    PlacingTheBet()
