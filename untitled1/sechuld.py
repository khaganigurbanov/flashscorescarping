import time
from selenium import webdriver
from bs4 import BeautifulSoup #pip install bs4

driver = webdriver.Firefox()

driver.get("https://www.flashscore.com/")
time.sleep(2)
elements = driver.find_elements_by_css_selector("div.tabs__tab")
elements[4].click()

def track_matches(container):
    soup = BeautifulSoup(container, "html.parser")
    matches = soup.select(".event__match.event__match--oneLine.event__match--scheduled")
    for match in matches:
        #country = match.select_one("span.event__title - -name")
        team1 = match.select_one("div.event__participant.event__participant--home")
        team2 = match.select_one("div.event__participant.event__participant--away")
        total = match.select_one("div.event__scores.fontBold")
        id_match = match["id"].split("_")[-1] # g_1_ b9HDyRiE
        print( team1.text , total.text , team2.text )






while True:
        container = driver.find_element_by_css_selector("div[id=live-table]").get_attribute("innerHTML")
        track_matches(container)




        import time
from selenium import webdriver
from bs4 import BeautifulSoup #pip install bs4

driver = webdriver.Firefox()

driver.get("https://www.flashscore.com/")
time.sleep(2)
elements = driver.find_elements_by_css_selector("div.tabs__tab")
elements[4].click()

def track_matches(container):
    soup = BeautifulSoup(container, "html.parser")
    matches = soup.select(".event__match.event__match--oneLine.event__match--online")
    for match in matches:
        #country = match.select_one("span.event__title - -name")
        team1 = match.select_one("div.event__participant.event__participant--home")
        team2 = match.select_one("div.event__participant.event__participant--away")
        total = match.select_one("div.event__scores.fontBold")
        id_match = match["id"].split("_")[-1] # g_1_ b9HDyRiE
        print( team1.text , total.text , team2.text )






while True:
        container = driver.find_element_by_css_selector("div[id=live-table]").get_attribute("innerHTML")
        track_matches(container)



        #oyunlarin olkelerle cekilmish hali

        driver.get("https://www.flashscore.com/")
time.sleep(80)
elements = driver.find_elements_by_css_selector("div.tabs__tab")
elements[4].click()


def track_matches(container):
    templiga =""
    templiga2 = ""
    soup = BeautifulSoup(container, "html.parser")
    matches = soup.find_all("div")

    for div in matches:

        liga1 = div.select_one("span.event__title--type")
        liga2 = div.select_one("span.event__title--name")
        if liga1 != None and liga2 != None and liga1 != templiga :

            #print(liga1.text , liga2.text)
            templiga = liga1
            templiga2 = liga2

        team1      = div.select_one("div.event__participant--home")
        team2      = div.select_one("div.event__participant--away")
        matchtime  = div.select_one("div.event__time")

        if team1 != None and  team2 != None:
            print( matchtime.text , templiga.text, templiga2.text, team1.text , team2.text)
            print ("===========")


#gunun oyunlari olkeler sechilmekle










container = driver.find_element_by_css_selector("div[id=live-table]").get_attribute("innerHTML")
track_matches(container)