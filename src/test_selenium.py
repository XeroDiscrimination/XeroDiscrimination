import time
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

# driver = Chrome(executable_path='/opt/WebDriver/bin/chromedriver')

# # with Chrome() as driver:
#     #your code inside this indent
# driver.get("http://127.0.0.1:8000/")
# time.sleep(2)

# driver.find_element_by_id('icon_ZeroDiscrimination').click()
# time.sleep(1)

# driver.find_element_by_xpath('//a[contains(text(), "Home")]').click()

# # assert driver.current_url == "http://127.0.0.1:8000/"
# driver.find_element_by_xpath('//a[contains(text(), "About Us")]').click()

# time.sleep(5)
# driver.close()
# driver.quit()

def wait(x):
    time.sleep(x)

class AutomatedTest(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome(executable_path='/opt/WebDriver/bin/chromedriver')
        self.driver.get("http://127.0.0.1:8000/")
        # self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        wait(2)

    def test_navBar(self):
        # Arrange
        driver = self.driver
        # Act: click links in NavBar should go to corresponding page
        click1 = driver.find_element_by_xpath('//a[contains(text(), "Zero Discrimination")]').click()
        click2 = driver.find_element_by_xpath('//a[contains(text(), "Home")]').click()
        click3 = driver.find_element_by_xpath('//a[contains(text(), "About Us")]').click()
        click4 = driver.find_element_by_xpath('//a[contains(text(), "Partners")]').click()
        click5 = driver.find_element_by_xpath('//a[contains(text(), "Contact")]').click()
        # Assert
        self.assertEqual("http://127.0.0.1:8000/", click1.current_url, "Click navBar ZeroDiscrimination should go to index page")
        self.assertEqual("http://127.0.0.1:8000/", click2.current_url, "Click navBar Home should go to index page")
        self.assertEqual("http://127.0.0.1:8000/about/", click3.current_url, "Click navBar About Us should go to about page")
        self.assertEqual("http://127.0.0.1:8000/rainbow_tick/", click4.current_url, "Click navBar About Us should go to rainbow_tick page")
        self.assertEqual("http://127.0.0.1:8000/contact/", click5.current_url, "Click navBar About Us should go to contact page")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()