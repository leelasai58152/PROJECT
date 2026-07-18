from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
class Leave:

    login_txt=(By.NAME,"username")
    password_txt=(By.NAME,"password")
    login_btn = (By.XPATH,"//button[@type='submit']")

    leave_btn=(By.XPATH,"//a[@href='/web/index.php/leave/viewLeaveModule']")
    from_date_txt=(By.XPATH,"//input[@placeholder='yyyy-dd-mm']")
    
    
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,20)
    
    def login(self,username,password):
        self.wait.until(EC.visibility_of_element_located(self.login_txt)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password_txt)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()
        
    def leave_click(self):
        self.wait.until(EC.element_to_be_clickable(self.leave_btn)).click()
        
    def from_date(self,date):
        element=self.wait.until(EC.element_to_be_clickable(self.from_date_txt))
        element.click()
        element.send_keys(Keys.CONTROL,"a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)
        
        
    def all_leave(self,username,password,date):
        self.login(username,password)
        self.leave_click()
        self.from_date(date)
        