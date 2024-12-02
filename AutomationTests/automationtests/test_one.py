import pytest
from pageObjects.PlaceTheBet import PlaceBet
import asyncio
from playwright.async_api import Page, expect, async_playwright

pytest_plugins = ('pytest_asyncio',)
@pytest.mark.asyncio
async def test_place_bet():
    async with async_playwright() as p:
        browser =await p.chromium.launch(headless=False)
        context =await browser.new_context()
        page = await context.new_page()
        objectPlaceBet = PlaceBet(page)
        await objectPlaceBet.navigate()
        # game selection:

        await objectPlaceBet.selectTheGame()
        #get the balance initial:
        balance_value =await objectPlaceBet.getTheBalance()
        await objectPlaceBet.selectTheValue()
        # The placed bet:
        amount_value =await objectPlaceBet.getTheAmountValue()

        #place the bet:
        await asyncio.sleep(10)
        await objectPlaceBet.placeTheBet()
        await page.wait_for_timeout(2000)
        # when the bet is placed:
        new_balance_value = await objectPlaceBet.getTheBalance()
        sum_of_elements = new_balance_value + amount_value
        print(new_balance_value)
        print(balance_value)
        await asyncio.sleep(40)

        assert (sum_of_elements) == balance_value, (
            f"Test failed: Expected {(new_balance_value + amount_value)} "
            f"to equal {balance_value}, got {sum_of_elements}"
        )
        await browser.close()
@pytest.mark.asyncio
async def test_cash_out():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        objectPlaceBet = PlaceBet(page)
        await objectPlaceBet.navigate()
        await objectPlaceBet.selectTheGame()
        # get the balance initial:
        balance_value = await objectPlaceBet.getTheBalance()
        await objectPlaceBet.selectTheValue()
        # The placed bet:
        amount_value = await objectPlaceBet.getTheAmountValue()

        # place the bet:
        await asyncio.sleep(10)
        await objectPlaceBet.placeTheBet()

        val_aftercash = await objectPlaceBet.cashOutValue()
        print(val_aftercash)
        browser.close()



        #cashing out:




