from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    login_txt=(By.NAME,"username")
    password_txt=(By.NAME,"password")
    login_btn = (By.XPATH,"//button[@type='submit']")
    def __init__ (self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,20)
    
    def login(self,username):
        
        self.wait.until(EC.visibility_of_element_located(self.login_txt)).send_keys(username)
        
    def password(self,password):
        self.wait.until(EC.visibility_of_element_located(self.password_txt)).send_keys(password)
        
    def login_butn(self):
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()
        
    def all_login(self,username,password):
        self.login(username)
        self.password(password)
        self.login_butn()
        