#-*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Dane testowe

gender = 'M'
country_code = '+48'
invalid_email = '123@wp.pl'
valid_phone_number = '572159878'

class WizzCheck(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def test_Wizz(self):
        driver = self.driver
        driver.get("https://wizzair.com/pl-pl/main-page#/")

        # Kliknij zaloguj przycisk
        zal_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="navigation-menu-signin"]')))
        zal_btn.click()

        # Kliknij rejestracja
        rej_btn = driver.find_element_by_xpath('//button[text()=" Rejestracja "]')
        rej_btn.click()

        # Wprowadz imie
        inp_imie = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-1"]/label[1]/div[1]/input')
        inp_imie.send_keys('Grzegorz')

        # Wprowadz nazwisko
        inp_nazw = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-1"]/label[2]/div[1]/input')
        inp_nazw.send_keys('Wojnowski')

        # Wybierz Plec

        # Wybierz mezczyzna
        if gender == 'M':
            m = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-2"]/div[1]/label[2]/span')
            m.click()
        # Wybierz kobieta
        else:
            f = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-2"]/div[1]/label[1]/span')
            f.click()

        # Wybierz kod kraju
        

        # Wprowadz numer telefonu
        driver.find_element_by_name("phoneNumberValidDigits").send_keys(valid_phone_number)

        # Wprowadz adres email
        driver.find_element_by_name("email").send_keys(invalid_email)

        # Wybierz kobieta


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
