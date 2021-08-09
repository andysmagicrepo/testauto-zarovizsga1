# ** 2 Feladat: Pénzfeldobás
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a pénzfeldobás app-ot az [https://black-moss-0a0440e03.azurestaticapps.net/tts4.html](https://black-moss-0a0440e03.azurestaticapps.net/tts4.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a pénzfeldobás app tesztelését.
#
# Az alkalmazás akkor működik helyesen ha 100 gombnyomásból legalább 30 fej. Ezt kell ellenőrizned.
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `tts4.py`
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
    driver.get('https://black-moss-0a0440e03.azurestaticapps.net/tts4.html')
    time.sleep(2)

    # valtozok inicializalasa
    penzfeldobas_button = driver.find_element_by_id("submit")
    utolso_eredmeny = driver.find_element_by_id("lastResult")
    fejszam = 0

    # TC1
    # 100 pénzfeldobas szimulacio
    # Az alkalmazás akkor működik helyesen ha 100 gombnyomásból legalább 30 fej.\
    # Ezt kell ellenőrizned.
    for i in range(1, 100):
        penzfeldobas_button.click()
        szoveg = utolso_eredmeny.text
        if szoveg == 'fej':
            fejszam += 1
    assert fejszam >= 30

except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    driver.close()
    driver.quit()

