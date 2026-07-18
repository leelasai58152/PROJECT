from pages.leave_page import Leave
from utils.config import *
from pages.my_info import Myinfo

def test_leave(setup):
    driver=setup
    driver.get(URL)
    
    login=Leave(driver)
    login.all_leave(USERNAME,PASSWORD,"2001-03-03")
    
    info=Myinfo(driver)
    info.all_info("abcd")
    
    assert 'viewPersonalDetails' in driver.current_url