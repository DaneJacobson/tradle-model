from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

import const

# Specify the path to the chromedriver.exe
webdriver_service = Service(const.DRIVER_PATH)

# Set up options for the driver (like headless mode)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Runs Chrome in headless mode.

# Set up the driver
driver = webdriver.Chrome(service=webdriver_service, options=options)

# The URL you want to open
url = "https://oec.world/api/olap-proxy/data?cube=trade_i_baci_a_92&drilldowns=Year,HS4&measures=Trade%20Value&parents=true&Year=2021&Exporter%20Country=nausa"

# Open the URL
driver.get(url)

# Wait for the page to load
time.sleep(5)  # Adjust this according to your needs

# Now, you can access the HTML content of the page
page_source = driver.page_source
print(page_source)  # This will print the HTML source code of the page

# Close the browser
driver.quit()
