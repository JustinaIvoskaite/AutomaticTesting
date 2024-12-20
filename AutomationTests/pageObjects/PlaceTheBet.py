from BaseFunctions import baseFunctions
class PlaceBet(baseFunctions):
    def __init__(self, page):

        super().__init__(page)
        #locators
        self.iframe = page.frame_locator("#betgames_iframe")
        self.element_of_game = self.iframe.locator("a[data-qa='area-game-card-27']")
        self.balance_element = self.iframe.locator("[data-qa='text-balance-amount']")
        self.amount_input = self.iframe.locator("input.bet-slip-input.BetslipSkyward_input__Jk56w").first
        self.amountValueClick = self.iframe.locator("[data-qa='button-bet-slip-amount-10']").first
        self.button_place = self.iframe.locator("[data-qa='button-place-bet']").first
        self.cash_out  = self.iframe.get_by_role("button", name="Cash out")
        self.title_button = self.cash_out.locator("div.PlaceBetButton_title__TdI-T")
        self.valueCashOut = self.cash_out.locator("div.PlaceBetButton_win__M+PSA")
        #cash out:

    async def navigate(self):
        await self.page.goto("https://demo.betgames.tv")
    async def selectTheGame(self):
        await self.element_of_game.wait_for(state="visible")
        await self.element_of_game.click()

    async def getTheBalance(self):
        await self.balance_element.wait_for(state="attached")
        await self.balance_element.wait_for(state="visible")
        balance_text = await  self.balance_element.text_content()
        balance_value = float(balance_text.replace("€", "").replace(",", ""))
        return balance_value

    async def selectTheValue(self):
        await self.amountValueClick.wait_for(state="visible")
        await self.amountValueClick.click()

    async def getTheAmountValue(self):

       self.amount_input.wait_for(timeout=5000)
       amount_value_t =float(await self.amount_input.get_attribute("value"))
       return amount_value_t

    async def placeTheBet(self):
            await self.button_place.wait_for(state="visible", timeout = 5000)
            await self.button_place.click()

    async def getTheNewValue(self):
        new_balance_text = await self.balance_element.text_content()
        new_balance_value = float(new_balance_text.replace("€", "").replace(",", ""))
        return new_balance_value

    async def cashOutValue(self):
        await self.cash_out.wait_for(state = "visible", timeout=30000)
        await self.cash_out.click()
        value_get = await self.valueCashOut.text_content()
        return value_get




