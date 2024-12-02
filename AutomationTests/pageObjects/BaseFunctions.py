class baseFunctions():
    def __init__(self, page):
        self.page = page
        self.iframe = page.frame_locator("#betgames_iframe")

    async def navigate(self):
        await self.page.goto("https://demo.betgames.tv")

    '''
    async def selectTheGame(self):
        await self.element_of_game.wait_for(state="visible")
        await self.element_of_game.click()
    '''









