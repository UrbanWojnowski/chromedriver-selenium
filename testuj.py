# Import modulu unittest
import unittest
# Import webdrivera
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

email= "tester@wsb.pl"
gender = "male"
name = "Marcin"
surname = "Nowak"
password = "Qwertry123@@"
birth_day = "2"
birth_month = 'January '
birth_year = '2000'


# Tworze klase WsbPlCheck dziedziczaca po
# TestCase z modulu unittest
class APRegistration(unittest.TestCase):
    """Analogia: Przypadek/scenariusz testowy"""

    # Przygotowanie do kazdego testu
    # (Warunki wstepne)
    def setUp(self):
        self.driver = webdriver.Firefox()
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
        # 7. Sprawdz email
        # Pobierz atrubut value z webelementu
        email_fact = driver.find_element_by_id("email").get_attribute("value")
        # Wypisz te wartosc
        print("W polu jest email: ", email_fact)
        # Porownaj wartosc wyswietlana z wczesniej wpisywana
        assert email_fact == email
        # 8. Wpisz haslo
        driver.find_element_by_id("passwd").send_keys(password)
        # 9. Wpisz date urodzenia
        day =  Select(driver.find_element_by_id("days"))
        day.select_by_value(birth_day)
        month =  Select(driver.find_element_by_id("months"))
        month.select_by_visible_text(birth_month)
        year =  Select(driver.find_element_by_id("years"))
        year.select_by_value(birth_year)
        # Sleep do celow testowych, by zauwazyc co sie dzieje
        # 10. Sprawdz pole First name
        name_fact = driver.find_element_by_xpath('//input[@id="firstname"]').get_attribute("value")
        print("W polu jest imie: ", name_fact)
        # Porownaj imie, ktore wpisywalismy z tym wyswietlonym w polu
        assert name == name_fact
        # 11. Sprawdz pole Last name
        surname_fact = driver.find_element_by_xpath('//input[@name="lastname"]').get_attribute("value")
        print("W polu jest nazwisko: ", surname_fact)
        assert surname == surname_fact
        time.sleep(3)

# Uruchom test jesli uruchamiamy
# ten plik
if __name__ == "__main__":
    unittest.main()
