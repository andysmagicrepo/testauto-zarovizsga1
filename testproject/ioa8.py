# ** 3 Feladat: számoló
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a összeadó app-ot az [https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html](https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a összeadó app tesztelését.
#
# Az applikáció minden frissítésnél véletlenszerűen változik!
#
# A feladatod, hogy a random számokkal működő matematikai applikációt ellenőrizd. A teszted ki kell, hogy olvassa a két operandust (számot) és az operátort (műveleti jelet). Ennek megfelelően kell elvégezned a kalkulációt Pythonban.
#
# A kalkuláció gombra kattintva mutatja meg az applikáció, hogy mi a művelet eredménye szerinte.
#
# Hasonlítsd össze az applikáció által kínált megoldást és a Python által kalkulált eredményt. Ennek a kettőnek egyeznie kell.
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `ioa8.py`
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
    URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"
    driver.get(URL)
    time.sleep(5)

    # Érték es művelet mezők
    adat1 = driver.find_element_by_id('num1').text
    adat2 = driver.find_element_by_id('num2').text
    adat1_szam = int(adat1)
    adat2_szam = int(adat2)
    muvelet = driver.find_element_by_id('op').text
    # szamolás gomb
    szamol_gomb = driver.find_element_by_id('submit')
    szamol_gomb.click()
    # weblap eredmeny
    eredmeny_webpage = driver.find_element_by_id('result').text

    if muvelet == '*':
        eredmeny_szamolt = adat1_szam * adat2_szam
    elif muvelet == '/':
        eredmeny_szamolt = adat1_szam / adat2_szam
    elif muvelet == '+':
        eredmeny_szamolt = adat1_szam + adat2_szam
    elif muvelet == '-':
        eredmeny_szamolt = adat1_szam - adat2_szam
    else:
        print("Hibás művelet megadás")

    print(eredmeny_webpage)
    print(eredmeny_szamolt)
    time.sleep(5)
    assert eredmeny_szamolt == int(eredmeny_webpage)
    time.sleep(1)

except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    driver.close()
    driver.quit()
