class ContactTheService:
    def __init__(self, page):
        self.page = page
        #locators
        self.get_language_parent = page.locator("#language")
        self.email_input =  page.locator("#email")
        self.message_input = page.locator("#message")
        self.send_btn = page.locator(".send.btn.btn-primary.pull-left")
        self.success =page.locator("#send")
    async def navigate(self):
        await self.page.goto("https://demo.betgames.tv")

    async def fillContent(self, email, message):
        await self.email_input.wait_for(state="visible")
        await self.message_input.wait_for(state="visible")
        await self.send_btn.wait_for(state="visible")
        await self.email_input.fill(email)
        await self.message_input.fill(message)

    async def sendContent(self):
        await self.send_btn.click()

    async def getTheMessage(self):
        got_text = await self.success.text_content()
        return got_text