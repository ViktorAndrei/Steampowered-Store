from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import time

class BrowserTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://store.steampowered.com/")
        
    
    def test_store_buy_assert(self):
        self.driver.find_element(By.LINK_TEXT, "BUTIK").click()
        self.driver.find_element(By.XPATH, '//*[@id="store_nav_search_term"]').send_keys("Hogwarts Legacy")
        self.driver.find_element(By.XPATH, '//*[@id="search_suggestion_contents"]/a[1]/div[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btn_add_to_cart_822363"]/span').click()
        kundvagn = self.driver.find_element(By.XPATH, '//*[@id="cart_link"]')
        self.assertTrue(kundvagn.is_displayed)
        spel_text = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div[1]/div[2]/div[4]/div[1]/div[1]/div/div[1]/div[3]/a').text
        expected = 'Hogwarts Legacy'
        self.assertEqual(spel_text, expected)
        
    def test_store_search_assertItem(self):
        gemenskap = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[1]/div/div[2]/a[2]')
        a = ActionChains(self.driver)
        a.move_to_element(gemenskap).perform()
        self.driver.find_element(By.LINK_TEXT, 'MARKNAD').click()
        self.driver.find_element(By.XPATH, '//*[@id="findItemsSearchBox"]').send_keys("Revolution case")
        self.driver.find_element(By.XPATH,'//*[@id="result_0_name"]').click()
        item_name = self.driver.find_element(By.XPATH, '//*[@id="largeiteminfo_item_name"]').text
        expected = 'Revolution Case'
        self.assertEqual(item_name, expected)

    def test_login_assertAccount_logout(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="global_action_menu"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input').send_keys("Dumle212")
        self.driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input').send_keys("RAI548ium")
        self.driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="account_pulldown"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="account_dropdown"]/div/a[1]').click()
        profile_name = self.driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[1]/div[1]/span[1]').text
        expected = 'VaLn'
        self.assertEqual(profile_name, expected)
        self.driver.find_element(By.XPATH, '//*[@id="account_pulldown"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="account_dropdown"]/div/a[3]').click()

    def test_about_assertInstallButton(self):
        butik = self.driver.find_element(By.XPATH, '//*[@id="global_header"]/div/div[2]/a[1]')
        a = ActionChains(self.driver)
        a.move_to_element(butik).perform()
        self.driver.find_element(By.LINK_TEXT, 'OM').click()
        installation_button = self.driver.find_element(By.XPATH, '//*[@id="about_greeting"]/div[4]/div[1]/a')
        self.assertTrue(installation_button.is_displayed)

    def test_login_profile_lastPlayedGame_assertGame(self):
        #time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="global_action_menu"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input').send_keys("Dumle212")
        self.driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input').send_keys("RAI548ium")
        self.driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="account_pulldown"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="account_dropdown"]/div/a[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div[3]/a').click()
        game_name = self.driver.find_element(By.XPATH, '//*[@id="ModalContentContainer"]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]').text
        expected = 'Counter-Strike: Global Offensive'
        self.assertEqual(game_name, expected)
        


    def tearDown(self):
        self.driver.delete_all_cookies()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
