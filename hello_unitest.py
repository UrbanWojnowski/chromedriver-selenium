#import modul unittest
import unittest
import time
#import webdriver
from selenium import webdriver
# Tworze klase WsbPlCheck dziedziczaca po
# TestCase z modulu unittest
class WsbPlCheck(unittest.TestCase):
    """Analogia: Przypadek/scenariusz testowy"""

    # Przygotowanie do kazdego testu
    # (Warunki wstepne)
    def setUp(self):
        self.driver = webdriver.Chrome()
        time.sleep(3)

    # Sprzatanie po tescie
    def tearDown(self):
        self.driver.quit()

    # wlasciwy test
    def testWsb(self):
        self.driver.get("http://www.wsb.pl")

#Uruchom test jesli uruchamiamy
#ten plik
if __name__ == "__main__":
    unittest.main()
