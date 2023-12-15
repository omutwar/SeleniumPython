import time
# Selenium related imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

driver.get("https://www.yahoo.com/news")
top_menu_links = "(//ul[@class='_yb_q2cub'])[1]/li"

links = driver.find_elements("xpath", "//a[@href]")
print(f'*** Size of the links are: #{len(links)}')
print("----Printing all links found----")
# for link in links:
#     print(link.get_attribute("innerHTML"))
#     if "Science" or "science" in link.get_attribute("innerHTML"):
#         link.click()
#         break


print("----This is the end of all printed links----")
top_menu = driver.find_elements("xpath", top_menu_links)
for menu in top_menu:
    print(menu.get_attribute("innerHTML"))
    if "More" in menu.get_attribute("innerHTML"):
        menu.click()


driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

buttons = driver.find_elements("xpath", "//a[contains(., 'Paperback')]")
# Advanced XPath: //a[.//span[text()[contains(., "some text")]]]/span[text()[]contains(., 'S')]

for button in buttons:
    print(button.get_attribute("innerHTML").replace("&nbsp", " "))
