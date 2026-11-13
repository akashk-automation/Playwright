from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_login(page):

    page.goto("https://www.saucedemo.com")

    login_page = LoginPage(page)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    dashboard_page = DashboardPage(page)

    assert "inventory" in dashboard_page.get_page_url()