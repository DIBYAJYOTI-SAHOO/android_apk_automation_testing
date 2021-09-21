import time
import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Atg_app(unittest.TestCase):
    def setUp(self):
        desired_cap = {
            "deviceName": "emulator-5554",
            "platformName": "android",
            "appWaitDuration": "5000",
            "appActivity": "com.atg.world.activity.SplashActivity",
            "noReset": True,
            "appExecTimeout": "50000",
            "uiautomator2ServerLaunchTimeout": "50000",
            "uiautomator2ServerInstallTimeout": "50000",
            "appPackage": "com.ATG.World",
            "driver": "http://localhost:4723/wd/hub"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)


    def test_LoginWithRightCredential(self):
        self.driver.implicitly_wait(30)
        get_started = self.driver.find_element_by_id("com.ATG.World:id/getStartedTv")
        get_started.click()
        time.sleep(1)
        login_email = self.driver.find_element_by_id("com.ATG.World:id/login_email")
        login_email.click()
        email = self.driver.find_element_by_id("com.ATG.World:id/email")
        email.send_keys("wiz_saurabh@rediffmail.com")
        password = self.driver.find_element_by_id("com.ATG.World:id/password")
        password.send_keys("Pass@123")
        signin = self.driver.find_element_by_id("com.ATG.World:id/email_sign_in_button")
        signin.click()
        print("test_LoginWithRightCredential passed")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Atg_app)
    unittest.TextTestRunner(verbosity=1).run(suite)

