from pages.leave_page import Leave
from utils.config import *

def test_leave(setup):
    driver=setup
    driver.get(URL)
    
    login=Leave(driver)
    login.all_leave(USERNAME,PASSWORD,"2001-03-03")
    
   
    
    
    
    assert 'viewLeaveList' in driver.current_url