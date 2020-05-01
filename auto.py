
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

options = Options()
options.add_argument("--user-data-dir=./check")
driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)
driver.get("https://web.whatsapp.com/send?phone=918698800448&text=I%27m+interested+in+your+car+for+sale&source&data&app_absent=true")
#elements = driver.find_elements_by_class_name("._35EW6")

delay = 6 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME , '_35EW6')))
    print ("Message Sent!")
    driver.find_elements_by_class_name("_35EW6")[0].click()
except TimeoutException:
    print ("Loading took too much time!")

#