from pageObjectsProject.Contacts import ContactsPOM
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
        contacts = ContactsPOM(page)
        await contacts.navigate()

        await context.tracing.stop(path="C:\\Users\\37060\\Desktop\\trace.zip")
        await context.close()
        await browser.close()
