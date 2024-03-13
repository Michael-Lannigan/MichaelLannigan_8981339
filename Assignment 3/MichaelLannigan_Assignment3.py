# Importing required libraries
import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize a new driver (and the action chain, which we'll need later), go to the Bulbapedia main page, and maximize the window
# (The website can be quite laggy, but thankfully the webdriver seems to wait for the page to load before
# taking action; it's not just my time.sleep commands, it's waiting way longer than that.)
driver = webdriver.Chrome()
actionchain = webdriver.ActionChains(driver)
driver.get("https://bulbapedia.bulbagarden.net/wiki/Main_Page")
driver.maximize_window()

time.sleep(3)

# Search for the Pokémon Flygon by typing "flygon" into the search bar and pressing enter.
# (I was hoping that the various Pokémon pages would be regular enough that this could
# work for any Pokémon, but that's not the case; maybe in the future I'll be able to
# make it work in the general case, but that's far outside the scope of this assignment.)
searchbar = driver.find_element("name", "search")
searchbar.send_keys("flygon")
searchbar.send_keys(Keys.RETURN)

time.sleep(3)

# Go to the bottom of the table of Flygon's level up moves.
# (The elements we want are at the top, but if we try to go directly there, those elements
# will end up underneath an ad and can't be clicked, so we go here first)
bottomOfTable = driver.find_element("xpath", '//*[@id="mw-content-text"]/div[1]/table[15]/tbody/tr[3]')
actionchain.move_to_element(bottomOfTable)
time.sleep(1)

# Click on the button to sort the moves by power twice, sorting them in descending order of power.
# (The sorting button isn't actually an HTML element in itself -- credit goes to my girlfriend for figuring that part
# out for me -- which, as far as I can tell, means we need to actually move the mouse onto the element, shift it over a bit
# so it lines up with where it needs to be, and then click.)
sortByPower = driver.find_element("xpath", '//*[@id="mw-content-text"]/div[1]/table[15]/tbody/tr[2]/td/table/thead/tr/th[5]')
actionchain.move_to_element_with_offset(sortByPower, sortByPower.size["width"]*2/5, 0).click().perform()
time.sleep(1)
actionchain.move_to_element_with_offset(sortByPower, sortByPower.size["width"]*2/5, 0).click().perform()
time.sleep(1)

# Click on the top move in the list (which in this case is expected to be Boomburst, Flygon's strongest level up move).
strongestMove = driver.find_element("xpath", '//*[@id="mw-content-text"]/div[1]/table[15]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]')
strongestMove.click()

time.sleep(3)

# Click on the move's type (which in this case is expected to be Normal, as Boomburst is classified as a Normal type move).
# (Incidentally, this part does seem to work in the general case; during testing, the driver has clicked on the sort buttons
# incorrectly, thus taking me to the wrong move, a couple times, and in those cases, it will take me to that move's type.)
moveType = driver.find_element("xpath", '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[4]/td/table/tbody/tr[1]/td/a')
moveType.click()

time.sleep(3)

# Click on one of the types in the list of types visible on the right side of the page.
stellarType = driver.find_element("xpath", '//*[@id="mw-content-text"]/div[1]/div[1]/div[2]/div[1]/span')
time.sleep(1)
stellarType.click()

time.sleep(5)

# Close the driver.
driver.close()

# Four elements tested:
# 1) Sorting move list by power
# 2) Using a link from a Pokémon's level up move list to go to a move's page
# 3) Using the link from the infobox on a move's page to go to the page of that move's type
# 4) Using a link from the infobox on a type's page to go to another type's page