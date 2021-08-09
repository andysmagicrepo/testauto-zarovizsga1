# ** 1 Feladat: Keressük a téglalap kerületét
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a téglalap kerülete app-ot az [https://black-moss-0a0440e03.azurestaticapps.net/x234.html](https://black-moss-0a0440e03.azurestaticapps.net/x234.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a téglalap kerülete appban:
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!
#
# * Helyes kitöltés esete:
#     * a: 99
#     * b: 12
#     * Eredmény: 222
#
# * Nem számokkal történő kitöltés:
#     * a: kiskutya
#     * b: 12
#     * Eredmény: NaN
#
# * Üres kitöltés:
#     * a: <üres>
#     * b: <üres>
#     * Eredmény: NaN
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `x234.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
# * majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
# * ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
# * akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
# * a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
# * nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

def teglalap(x, y, z):
    a_input = driver.find_element_by_id("a")
    a_input.clear()
    a_input.send_keys(x)
    time.sleep(1)
    b_input = driver.find_element_by_id("b")
    b_input.clear()
    b_input.send_keys(y)
    time.sleep(1)
    kalkulacio_button = driver.find_element_by_id("submit")
    kalkulacio_button.click()
    time.sleep(3)
    result = driver.find_element_by_id("result")
    print(z)
    print(result.text)
    assert result.text == z

try:
    # Oldal betöltése
    driver.get('https://black-moss-0a0440e03.azurestaticapps.net/x234.html')
    time.sleep(2)

    #TC1
    # * Helyes kitöltés esete:
    #     * a: 99
    #     * b: 12
    #     * Eredmény: 222
    teglalap(99, 12, '222')

    # TC2
    # * Nem számokkal történő kitöltés:
    #     * a: kiskutya
    #     * b: 12
    #     * Eredmény: NaN
    teglalap('kiskutya', 12, 'NaN')

    #TC3
    # * Üres kitöltés:
    #     * a: <üres>
    #     * b: <üres>
    #     * Eredmény: NaN
    teglalap('', '', 'NaN')

except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    driver.close()
    driver.quit()