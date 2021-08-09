# * 4 Feladat: Email mező
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
# 
# A program töltse be a Email mező app-ot az [https://black-moss-0a0440e03.azurestaticapps.net/mm43.html](https://black-moss-0a0440e03.azurestaticapps.net/mm43.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a Email mező app tesztelését.
#
# A cél az email validáció tesztelése:
#
# * Helyes kitöltés esete:
#     * email: teszt@elek.hu
#     * Nincs validációs hibazüzenet
#
# * Helytelen:
#     * email: teszt@
#     * Please enter a part following '@'. 'teszt@' is incomplete.
#
# * Üres:
#     * email: <üres>
#     * b: <üres>
#     * Please fill out this field.
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `mm43.py`
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
    URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"
    driver.get(URL)
    time.sleep(5)
    email = driver.find_element_by_id("email")
    submit_button = driver.find_element_by_id("submit")

    #TC1
#Helyes kitöltés esete:
 #   * email: teszt@elek.hu
  #  * Nincs validációs hibazüzenet

    email.send_keys("teszt@elek.hu")
    submit_button.click()
    message = driver.find_element_by_class_name('validation-error').text
    print(message)
    #driver.find_element_by_xpath('//section[@id="container"]/div').is_displayed()
   # assert message.get_attribute('value') == ''
    time.sleep(2)

  #TC2
#Helytelen:
#email: teszt @
#Please enter a part following '@'. 'teszt@' is incomplete.
    email.clear()
    email.send_keys("teszt@")
    submit_button.click()
    time.sleep(5)
 #   assert message.text == "Please enter a part following '@'. 'teszt@' is incomplete."
    #message = driver.find_element_by_xpath('/html/body/div/div/p/form/div[@class="validation-error"]')
    #message = driver.find_element_by_xpath('/html/body/div/div/p/form/div[@class="validation-error"]')
    message = driver.find_element_by_class_name('validation-error')
    assert message.get_attribute('value') == 'Írjon be egy e-mail címet.'
    #a = message.get_attribute("value")
    print(message)

except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    driver.close()
    driver.quit()