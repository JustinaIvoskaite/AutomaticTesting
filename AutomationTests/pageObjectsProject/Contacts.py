from pageObjects.BaseFunctions import baseFunctions
class ContactsPOM():
    def __init__(self, page):
        self.page = page
        self.editButton_open = page.get_by_text("Redaguoti")
        self.vardasText = page.get_by_role("textbox", name="Vardas")
        self.pavText = page.get_by_role("textbox", name="Pavardė")
        self.telText = page.get_by_placeholder("Telefonas")
        self.elText = page.get_by_placeholder("Elektroninis paštas")
        self.vietaText = page.get_by_role("textbox", name="Vieta")
        self.export_open = page.get_by_text("Eksportuoti")
        self.saveButton = page.get_by_text("Pakeisti")
        self.deleteButton = page.get_by_text("Pašalinti")
        self.addButton_open = page.locator("svg.bi.bi-person-circle.icon-hover")
        self.delete= page.get_by_text("Taip")
        self.deleteNo = page.get_by_text("Ne")
    async def navigate(self):
        await self.page.goto("http://localhost:5173/contacts")
    async def openEdit(self):
        await self.editButton_open.wait_for(state ="visible")
        await self.editButton_open.click()
    async def fillContent(self):
        await self.vardasText.fill("testas")
        await self.pavText.fill("testas")
        await self.telText.fill("testas")
        await self.elText.fill("testas")
        await self.vietaText.fill("testas")
    async def selectSave(self):
        await self.saveButton.wait_for(state ="visible")
        await self.saveButton.click()





