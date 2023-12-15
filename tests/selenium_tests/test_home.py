from seleniumbase import BaseCase


class HomeTest(BaseCase):
    actual_title = 'Practice E-Commerce Site – SDET Unicorns – Helping you succeed in Software Quality.'
    base_url = 'https://practice.sdetunicorns.com/'

    def test_home_page(self):
        # open the website
        self.goto('https://practice.sdetunicorns.com/')

        # assert the web title
        self.assert_title(HomeTest.actual_title)

        # assert the logo
        pass
