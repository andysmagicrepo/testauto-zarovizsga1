# * 5 Feladat: Kakukktojás - városok
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a Kakukktojás - városok app-ot az [https://black-moss-0a0440e03.azurestaticapps.net/rv4.html](https://black-moss-0a0440e03.azurestaticapps.net/rv4.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a Kakukktojás - városok app tesztelését.
#
# Az applikáció minden frissítésnél véletlenszerűen változik!
#
# Feladatod, hogy megtaláld a hiányzó városnevet, kitöltsd a form-ban a mezőt és ellnörizd le, hogy eltaláltad-e.
#
# A feladatnak több helyes megoldása is van (találgatós/ismétlős, pythonban kalkulálós), mindegy, hogy hogyan oldod meg, csak találd meg az egy véletlen hiányzó város nevét
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `rv4.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
# * majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
# * ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
# * akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
# * a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
# * nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from pprint import pprint
import csv
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get('https://black-moss-0a0440e03.azurestaticapps.net/rv4.html')
    time.sleep(2)
    cities = driver.find_element_by_id('cites').text
    print(cities)

    random_cities = driver.find_element_by_id('randomCities').text
    # print(random_cities)
    # missing = set(random_cities) ^ set(cities)
    # missing = [item for item in random_cities if item not in cities]
    missing = list(set(cities) - set(random_cities))
    print(missing)

    # beírni a hiányzó várost
    missing_city_button = driver.find_element_by_id("missingCity")
    missing_city_button.send_keys(missing)
    submit_button = driver.find_element_by_id('submit')
    result = driver.find_element_by_id('result').text
    # assert result == ''

except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    driver.close()
    driver.quit()