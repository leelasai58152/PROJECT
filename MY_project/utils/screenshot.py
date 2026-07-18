import os
from datetime import datetime

def take_screenshot(driver,test_name):
    folder = "screenshot"
    if not os.path.exists(folder):
        os.makedirs(folder)
    time= datetime.now().strftime("%Y,%m,%d_%H,%M,%S")
    file= f"{folder}/{test_name}_{time}.png"
    driver.save_screenshot(file)
    return file