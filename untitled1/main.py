import time
import re
from selenium import webdriver ,common
from bs4 import BeautifulSoup #pip install bs4
from database import Database

# for find match function
match_css =".event__match.event__match--oneLine.event__match--scheduled.event__match--last"
#for next day
calendar_css =".calendar__direction.calendar__direction--tomorrow"
driver = webdriver.Firefox(executable_path="C:\\Users\\Xaqani\\Desktop\\geckodriver.exe")

driver.get("https://www.flashscore.com/")
time.sleep(10)
elements = driver.find_elements_by_css_selector("div.tabs__tab")
elements[4].click()
time.sleep(10)
html =  driver.find_element_by_css_selector("div[id=live-table]").get_attribute("innerHTML")
#calendar__datepicker

def find_match(html):
    #deyishenler
    data = []
    ids = 0
    template = "https://www.flashscore.com/match/{}/#match-summary"
    soup = BeautifulSoup(html, "html.parser")
    matches = soup.select(match_css)
    print(len(matches))
    for match in matches:
        time_match = match.select_one("div.event__time")
        team1      = match.select_one("div.event__participant.event__participant--home")
        team2      = match.select_one("div.event__participant.event__participant--away")
        id_match   = match["id"].split("_")[-1]  # g_1_ b9HDyRiE
        url        = template.format(id_match)

        if time_match != None and team1 != None and team2 != None:
            time_match = time_match.text.strip()
        ids = ids + 1
        data.append((ids , time_match, "country" , "league" ,  team1.text, team2.text, id_match , 1 , 0 , "0:0" , "2:0" ))
    #print(data)
    return data
        #print(ids, time_match, team1.text, team2.text, id_match)

def find_country(html):
    #Deyishenler
    tempData =[]
    templiga = ""
    templiga2 = ""
    soup = BeautifulSoup(html, "html.parser")
    matches = soup.find_all("div")

    for div in matches:
        time_match = div.select_one("div.event__time")
        liga1 = div.select_one("span.event__title--type")
        liga2 = div.select_one("span.event__title--name")
        team1 = div.select_one("div.event__participant--home")
        team2 = div.select_one("div.event__participant--away")


        if liga1 != None and liga2 != None :

            if templiga == "" and templiga2 == "":
                templiga = liga1.text
                templiga2 = liga2.text
            if templiga != liga1.text:
                templiga = liga1.text

            if templiga2 != liga2:
                templiga2 = liga2
        print(templiga, templiga2)
            #tempData.append((templiga , templiga2 , team1.text , team2.text))

    return tempData
    #print(tempData)
       # print(matchtime.text, templiga.text, templiga2.text, team1.text, team2.text)
#tarixlerin ireliye chevrilmesi

def nexted(firefox):

    time.sleep(2)
    next_btn = firefox.find_element_by_css_selector(calendar_css)
    next_btn.click()
    time.sleep(2)
    html = firefox.find_element_by_css_selector("div[id=live-table]").get_attribute("innerHTML")
    return html

for _ in range(10):
    try:
        html =nexted(driver)
        oyunlar =find_match(html)
        time.sleep(5)
        print(oyunlar)
    except common.exceptions.NoSuchElementException:
        print("End")
        break

time.sleep(2)




#find_match(html)
#find_country(html)




driver.close()
driver.quit()


