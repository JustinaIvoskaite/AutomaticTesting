from pageObjects.ContactService import ContactTheService
import asyncio
import helpers
import pytest
from playwright.async_api import Page, expect, async_playwright
@pytest.mark.asyncio
async def test_contact_service():

    async with async_playwright() as p:
        language_second = "English"
        browser = await p.chromium.launch(headless=False, slow_mo=2000)
        context = await browser.new_context()
        #tracing:
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        contactObj = ContactTheService(page)
        await contactObj.navigate()
        await asyncio.sleep(10)
        await contactObj.fillContent("kazkas@gmail.com", "Testavimo zinute")
        should_be = helpers.GetMessageByLanguage(language_second)
        await asyncio.sleep(10)
        await contactObj.sendContent()
        await asyncio.sleep(5)
        # message for success if sent
        #got_text = await contactObj.getTheMessage()
        await expect(contactObj.success).to_have_text(should_be);
        #assert got_text == should_be, f"Message is not correct. Expected: '{should_be}', Found: '{got_text}'"
        await context.tracing.stop(path="C:\\Users\\37060\\Desktop\\trace.zip")
        await context.close()
        await browser.close()

@pytest.mark.asyncio
async def test_contact_boxes():

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=2000)
        context = await browser.new_context()
        page = await context.new_page()
        contactObj = ContactTheService(page)
        await contactObj.navigate()
        await expect(contactObj.email_input).to_be_editable()
        await  expect(contactObj.message_input).to_be_editable()
        await expect(contactObj.send_btn).to
