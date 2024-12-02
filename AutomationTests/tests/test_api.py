from playwright.async_api import async_playwright
import pytest
import asyncio
from playwright.async_api import Page, expect, async_playwright
@pytest.mark.asynchio
async def test_api_call():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(base_url="http://localhost:8080/contacts")
        api_request_context = context.request
        page = await context.new_page()
        data_contacts = {
            "vardas": "testas",
            "pavarde": "testas",
            "telefonas": "testas",
            "el_pastas": "testas@gmail.com",
            "gyvenamoji_vieta": "testas",
            "fk_Adresu_knygeleid_Adresu_knygele": 1
        }
        BASE_URL = "http://localhost:8080"

        await api_request_context.fetch(f'{BASE_URL}/contacts/insertContacts', method="post", data=data_contacts)








