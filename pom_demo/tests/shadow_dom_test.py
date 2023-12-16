from selenium import webdriver


# Function to expand shadow root
def expand_shadow_element(element):
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root


# Instantiate the WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get('http://your-web-page-url.com')

# Find the shadow host
shadow_host = driver.find_element_by_id('shadow_host')

# Expand the shadow root
shadow_root = expand_shadow_element(shadow_host)

# Find the element within the shadow DOM
shadow_content = shadow_root.find_element_by_id('shadow_content')

# Check if the element is selected
is_checked = shadow_content.is_selected()

print(f'Is Checked: {is_checked}')

# Close the driver
driver.quit()
