class DashboardPage:

    def __init__(self, page):
        self.page = page

    def get_page_url(self):
        return self.page.url