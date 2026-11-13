class LoginPage:

    def __init__(self, page):
        self.page = page

    username = "#user-name"
    password = "#password"
    login_button = "#login-button"

    def login(self, username, password):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.login_button)