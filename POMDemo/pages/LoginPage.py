from selenium.webdriver.common.by import By


class LoginPage:
    """

    """

    def __init__(self, driver):
        self.driver = driver
        self.signin_button = (By.CSS, 'li > button.select-signin')
        self.signin_email_box = (By.NAME, "input[name='email']")
        self.signin_password_box = (By.CSS_SELECTOR, "input[name='password']")
        self.login_button = (By.CSS_SELECTOR, "button[name='submit_attempt']")

    def do_login(self, username: str):
        print(username)

    def enter_password(self, password: str):
        print(password)

