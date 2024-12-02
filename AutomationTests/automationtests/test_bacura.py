import pytest
from pageObjects.TestBakara import BakaraTesting
import asyncio
from playwright.async_api import Page, expect, async_playwright

pytest_plugins = ('pytest_asyncio',)
@pytest.mark.asyncio
async def test_bacura():
    async with async_playwright() as p:
        browser =await p.chromium.launch(headless=False)
        context =await browser.new_context()
        page = await context.new_page()
        objectBacara = BakaraTesting(page)
        await objectBacara.navigate()
        # game selection:

        await objectBacara.selectTheGame()
        await asyncio.sleep(10)
        await objectBacara.selectTheFirst()

        await  objectBacara.selectTheValue()
        # get the balance initial:
        amount_value = await objectBacara.getTheAmountValue()
        print(amount_value)


        await browser.close()


@pytest.mark.asyncio
async def test_bacara_first():

    async with async_playwright() as p:
        browser =await p.chromium.launch(headless=False)
        context =await browser.new_context()
        page = await context.new_page()
        objectBacara = BakaraTesting(page)
        await objectBacara.navigate()

        await objectBacara.selectTheGame()
        await asyncio.sleep(10)

        expect(objectBacara.player_wins).to_be_disabled()
@pytest.mark.asyncio
async def test_bacara_tie():

    async with async_playwright() as p:
        browser =await p.chromium.launch(headless=False)
        context =await browser.new_context()
        page = await context.new_page()
        objectBacara = BakaraTesting(page)
        await objectBacara.navigate()
        await objectBacara.selectTheGame()
        await asyncio.sleep(10)
        expect(objectBacara.tie).to_be_disabled()

@pytest.mark.asyncio
async def test_bacara_bancer():
    async with async_playwright() as p:
        browser =await p.chromium.launch(headless=False)
        context =await browser.new_context()
        page = await context.new_page()
        objectBacara = BakaraTesting(page)
        await objectBacara.navigate()
        await objectBacara.selectTheGame()
        await asyncio.sleep(10)
        expect(objectBacara.banker).to_be_disabled()
