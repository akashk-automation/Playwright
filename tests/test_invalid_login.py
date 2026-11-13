from pages.login_page import LoginPage

def test_invalid_login(page):

    page.goto("https://www.saucedemo.com")

    login_page = LoginPage(page)

    login_page.login(
        "standard_user",
        "wrong_password"
    )

    error_message = page.locator("[data-test='error']").text_content()

    assert "Username and password do not match" in error_message