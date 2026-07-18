from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Myinfo:
    my_infobtn=(By.XPATH,"//a[@href='/web/index.php/pim/viewMyDetails']")
    first_name=(By.XPATH,"//input[@placeholder='First Name']")
    
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,20)
    def my_info(self):
        self.wait.until(EC.element_to_be_clickable(self.my_infobtn)).click()
        
    def first_nam(self,first):
        self.wait.until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader"))
    )
        element=self.wait.until(EC.element_to_be_clickable(self.first_name))
        element.click()
        element.send_keys(Keys.CONTROL,"a")
        
        element.send_keys(first)
    def all_info(self,first):
        self.my_info()
        self.first_nam(first)