from pages.login_page import LoginPage
from utils.config import *

def test_login(setup):

    driver = setup
    driver.get(URL)
    
    
    login=LoginPage(driver)
    login.all_login(USERNAME,PASSWORD)
    
    assert 'dashboard'in driver.current_url.lower()
    
    
    
   
    
