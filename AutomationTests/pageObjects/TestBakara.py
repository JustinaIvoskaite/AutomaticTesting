from pageObjects.BaseFunctions import baseFunctions
class BakaraTesting(baseFunctions):
    def __init__(self, page):
        #navigation inherit:
        super().__init__(page)
        # locators
        self.iframe = page.frame_locator("#betgames_iframe")
        self.element_of_game = self.iframe.locator("a[data-qa='area-game-card-6']")
        #-------------main bets------------------
        self.player_wins = self.iframe.locator("[data-qa='area-odd-item-469']")
        self.banker = self.iframe.locator("[data-qa='area-odd-item-470']")
        self.tie = self.iframe.locator("[data-qa='area-odd-item-471']")
        #colours section:
        self.colours = self.iframe.locator("[data-qa='button-odds-tab-37']")
        self.select_val = self.iframe.locator("[data-qa='button-bet-slip-amount-100']")
        self.amount_ = self.iframe.locator("input.AmountInput_input__cm5YJ.bet-slip-input").first
        self.place_bet = self.iframe.locator("button.PlaceBetButton_container__l38H3.place-bet-button")
        self.balance_element = self.iframe.locator("[data-qa='text-balance-amount']")

    async def selectTheGame(self):
        await self.element_of_game.wait_for(state="visible")
        await self.element_of_game.click()

    async def selectTheFirst(self):
        await self.player_wins.wait_for(state="visible")
        await self.player_wins.click()

    async def selectTheSecond(self):
        await self.banker.wait_for(state="visible")
        await self.element_of_game.click()

    async def selectTheThird(self):
        await self.tie.wait_for(state="visible")
        await self.element_of_game.click()
    async def selectTheValue(self):

        await self.select_val.wait_for(state="visible")
        await self.select_val.click()
    async def getTheAmountValue(self):

       self.amount_.wait_for(timeout=5000)
       amount_value_t =float(await self.amount_.get_attribute("value"))
       return amount_value_t

    async def placeTheBet(self):
        await self.place_bet.wait_for(state="visible", timeout=5000)
        await self.place_bet.click()

    async def getTheBalance(self):
        await self.balance_element.wait_for(state="attached")
        await self.balance_element.wait_for(state="visible")
        balance_text = await  self.balance_element.text_content()
        balance_value = float(balance_text.replace("€", "").replace(",", ""))
        return balance_value

    #colors testing, more reds drawn?:
    async def selectTheColours(self):
        await self.colours.wait_for(state="visible")
        await self.colours.click()





