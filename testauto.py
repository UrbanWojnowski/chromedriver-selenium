# Import modulu unittest
import unittest
# Import webdrivera
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

email= "tester@wsb.pl"
gender = "male"
name = "Grzegorz"
surname = "Wojnowski"


# Tworze klase WsbPlCheck dziedziczaca po
# TestCase z modulu unittest
class APRegistration(unittest.TestCase):
    """Analogia: Przypadek/scenariusz testowy"""

    # Przygotowanie do kazdego testu
    # (Warunki wstepne)
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        # Czekaj max 5 sekund na elementy
        self.driver.implicitly_wait(15)
    # Sprzatanie po kazdym tescie
    def tearDown(self):
        self.driver.quit()

    #Wlasciwy test
    # nazwa musi zaczynac sie od slowa test
    def testCorrectRegistration(self):
        # 1. Kliknij login
        driver = self.driver
        signin = driver.find_element_by_class_name("login")
        signin.click()
        # 2. Wpisz email
        email_input = driver.find_element_by_id("email_create")
        email_input.send_keys(email)
        # 3. Kliknij Create account
        create_account_btn = driver.find_element_by_id("SubmitCreate")
        create_account_btn.click()
        # 4. Wybierz plec
        if gender == "male":
            driver.find_element_by_id("id_gender1").click()
        elif gender=="female":
            driver.find_element_by_id("id_gender2").click()
        # 5. Wpisz imie
        driver.find_element_by_id("customer_firstname").send_keys(name)
        # 6. Wpisz nazwisko
        driver.find_element_by_id("customer_lastname").send_keys(surname)
        # 7. Sprawdz email_fact
        # Pobierz atrybut value z webelement
        email_fact = driver.find_element_by_id("email").get_attribute("value")
        # Wypisz te wartosc
        print(email_fact)
        # Porownaj wartosc wyswietlona z wczesniej wypisana
        assert email_fact == email

        # dla daty urodzenia
        day = Select(driver.find_element_by_id("days"))
        day.select_by_value("6")
        month = Select(driver.find_element_by_id("months"))
        month.select_by_visible_text('February ')
        year = Select(driver.find_element_by_id("years"))
        year.select_by_value("1977")


        # Sleep do celow testowych, by zauwazyc co sie dzieje
        time.sleep(3)

# Uruchom test jesli uruchamiamy
# ten plik
if __name__ == "__main__":
    unittest.main()
