from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest

class BrowserTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        serv_obj = Service("C:\Drivers\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=serv_obj)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://store.steampowered.com/")
        #self.mywait.until(EC.element_to_be_clickable((By.XPATH,"(//a[normalize-space()='Acceptera'])[1]"))).click()

    
    def test_link_path(self):
        self.driver.find_element(By.LINK_TEXT, "BUTIK").click()
        self.driver.find_element(By.XPATH, '//*[@id="store_nav_search_term"]').send_keys("Hogwarts Legacy")
        self.driver.find_element(By.XPATH, '//*[@id="search_suggestion_contents"]/a[1]/div[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btn_add_to_cart_822363"]/span').click()
        kundvagn = self.driver.find_element(By.XPATH, '//*[@id="cart_link"]')
        self.assertTrue(kundvagn.is_displayed)
        spel_text = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div[1]/div[2]/div[4]/div[1]/div[1]/div/div[1]/div[3]/a').text
        expected = 'Hogwarts Legacy'
        self.assertEqual(spel_text, expected)
        







    def tearDown(self):
        self.driver.delete_all_cookies()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()