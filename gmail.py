from selenium import webdriver
from time import sleep

DRIVER_PATH = 'driver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get("https://www.gmail.com")
sleep(2)
print("sleep 2 ends here")
driver.find_element_by_name("identifier").send_keys("nvmlogo@gmail.com")

driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/span").click()

driver.implicity_wait(4)

driver.find_element_by_name("password").send_keys("mobile016")
# driver.find