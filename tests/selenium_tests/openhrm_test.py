import pytest
import allure
from seleniumbase import BaseCase


@allure.severity(allure.severity_level.NORMAL)
class OpenHRMTest(BaseCase):
    openHRM_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def test_login(self):
        self.goto(OpenHRMTest.openHRM_url)
        self.fill("//input[@placeholder='Username']", "Admin")
        self.fill("//input[@placeholder='Password']", "admin123")
        self.click("//button[@type='submit']")
        self.assert_text_visible("Dashboard",
                                 "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

    def test_add_user(self):
        allure.attach(self.save_screenshot_after_test)
        pytest.skip("This is temp skipped test")

    def test_update_user(self):
        allure.attach(self.save_screenshot_after_test)
        pytest.fail("This is deliberately failed test")

    @pytest.fixture(autouse=True)
    def add_screenshot_on_failure(self, request):
        yield
        if request.node.rep_call.failed:
            self.save_screenshot(request.node.name + ".png")
