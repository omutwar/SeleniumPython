import allure
from seleniumbase import BaseCase


@allure.severity(allure.severity_level.NORMAL)
class HomeTest(BaseCase):
    actual_title = 'Practice E-Commerce Site – SDET Unicorns – Helping you succeed in Software Quality.'
    base_url = 'https://practice.sdetunicorns.com/'
    expected_message = "Think different. Make different."

    def test_home_page(self):
        # open the website
        self.goto(HomeTest.base_url)

        # assert the web title
        self.assert_title(HomeTest.actual_title)

        # assert the logo
        self.assert_element_present("//img[@alt='Practice E-Commerce Site']")

    def test_click_get_started(self):
        # open the website
        self.goto(HomeTest.base_url)

        # click on 'Get Started'
        self.click("//span[contains(text(), 'get started')]")

        # Check if the url contains 'Get Started' or not
        self.assert_url_contains("get-started")

    def test_text_displayed(self):
        self.open(HomeTest.base_url)

        text_displayed = self.get_text("h1.elementor-heading-title")
        print(text_displayed)

        self.assertTrue("Think different" in HomeTest.expected_message)

    def test_menu_links(self):
        expected_links = ["Home", "About", "Shop", "Blog", "Contact", "My account"]
        # open the url
        self.go_to(HomeTest.base_url)

        # find menu links
        # CSS:  #zak-primary-menu li[id*=menu-item]
        # id --> //ul[@id='zak-primary-menu']/li[starts-with(@id,'menu-item-')]
        menu_items = self.find_elements("//ul[@id='zak-primary-menu']/li[starts-with(@id,'menu-item-')]")
        print('')
        for index, item in enumerate(menu_items):
            self.assert_equal(expected_links[index], item.text)
            print("Index: {}, Actual Text: {}, Expected Text: {}".format(index, item.text, expected_links[index]))
            # print("Actual Text: {}, Expected Value: {}".format(item.text, expected_links[index]))
