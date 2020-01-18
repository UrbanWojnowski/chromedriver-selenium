#import modul unittest
import unittest
import time

email = "ugwojnowski@gmail.pl"
gender = "male"

#import webdriver
from selenium import webdriver
# Tworze klase WsbPlCheck dziedziczaca po
# TestCase z modulu unittest
class APRegistration(unittest.TestCase):
    """Analogia: Przypadek/scenariusz testowy"""

    # Przygotowanie do kazdego testu
    # (Warunki wstepne)
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    # Sprzatanie po tescie
    def tearDown(self):
        self.driver.quit()

    # wlasciwy test
    def testCorrectRegistration(self):
        # 1.kliknij login
        driver = self.driver
        signin = driver.find_element_by_class_name("login")
        signin.click()
        # 2. wpisz email
        email_input = driver.find_element_by_id("email_create")
        email_input.send_keys(email)
        # 3. Kliknij create account
        create_account_btn = driver.find_element_by_id("SubmitCreate")
        create_account_btn.click()
        # 4. wybierz plec
        if gender == "male":
            driver.find_element_by_id("id.gender1").click()
        elif gender == "female":
            driver.find_element_by_id("id.gender2").click()

        #time.sleep(3)

#Uruchom test jesli uruchamiamy
#ten plik
if __name__ == "__main__":
    unittest.main()
