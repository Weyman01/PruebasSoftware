import unittest
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class registro(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\driver_chrome\chromedriver.exe')

    def test_registry(self):
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/sale.html")

        account_btn = driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a')
        account_btn.click()
        time.sleep(1)
        registry  = driver.find_element_by_xpath('//*[@id="header-account"]/div/ul/li[5]/a')
        registry.click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="firstname"]').send_keys('Patata')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="middlename"]').send_keys('Master')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="lastname"]').send_keys('Weyman')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="email_address"]').send_keys('emailExample@gmail.com')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('ContraseñaC00L#')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="confirmation"]').send_keys('ContraseñaC00L#')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="form-validate"]/div[1]/ul/li[4]/label').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span').submit()

        time.sleep(5)

    def setDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()



