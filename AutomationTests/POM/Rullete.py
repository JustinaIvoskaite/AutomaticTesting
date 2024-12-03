from POM.baseClass import BaseClass
class Rullete(BaseClass):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.rullete = self.page.get_by_role("link", name='Roulettes')
        self.number = self.page.get_by_role("button", name="1 6")
        self.balance = self.page.locator("#username-comp-cash-amount")
        self.number2 = self.page.get_by_role("button", name="15")
        self.placeBet =  self.page.get_by_text("Place a bet")
        self.chip = self.page.locator("#roulette-chip-10")

    def getBalance(self):
        return float(self.balance.replace("€", "").replace(",", ""))

    def placeNumbers(self):
        self.number.click()
        self.chip.click()
        self.number2.click()

    def placeTheBet(self):
        self.placeBet.click()



















