
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


options = Options()
options.add_argument("--user-data-dir=./check")



def send(contact,msg):

    for no in contact:
       driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)
       driver.get('https://web.whatsapp.com/send?phone='+ str(no) +'&text='+ msg +'&source&data&app_absent=true')
       delay = 10 # seconds
       try:
           myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME , '_35EW6')))
           driver.find_elements_by_class_name("_35EW6")[0].click()
           print ("Message Sent to ", no ,"\n")
           time.sleep(3)
           driver.close()
       except TimeoutException:
           print ("Loading took too much time!")


contact = [
    919049481501,
    918526262648,
    918698800448,
    919168238924
]

send(contact,'testing multiple contact msgs');

