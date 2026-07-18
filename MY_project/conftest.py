import pytest
from utils.screenshot import take_screenshot
from utils.driver import get_driver


@pytest.fixture
def setup():
    driver=get_driver()
    yield driver
    driver.quit()
    
@pytest.hookimpl(hookwrapper=True)
def hook(item):
    outcome=yield
    report= outcome.get_result()
    if report.when=='call' and report.failed:
        driver=item.funcargs('item')
        take_screenshot(driver,item.name)
