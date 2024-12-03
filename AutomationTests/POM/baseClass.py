class BaseClass:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://qa-test.online.advbet.com/sports/football")



