from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = "http://www.dota2.com/leaderboards/#americas-0"
chrome_driver_path = './chromedriver_v90.exe'

print("Loading options...")
#Additional chromedriver options
chrome_options = Options()
chrome_options.add_argument("--headless")                                       #chromedriver perform in the background
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])   #chromedriver without a console message

print("Loading Chrome driver...")
#driver = webdriver.Chrome('./chromedriver_v91.exe')
driver = webdriver.Chrome(executable_path = chrome_driver_path, options = chrome_options)
driver.get(url)

print("Waiting...")
time.sleep(5) 
  
print("Parsing data...")
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

print("Finding players...")
table = soup.find('table')
tbody = table.find('tbody')
tbody = soup.find("tbody", attrs={"id": "leaderboard_body"})

print("Storing players...")
players = []
for item in tbody.find_all('tr'):
    players.append(item.text)
driver.close()
print("Done.\n")

#Function to print the length of players
def print_player_num():
    print("There are " + str(len(players)) + " immortal ranked players in North America.")

#Function to get the top 5 players
def print_top_five():
    for index in range(0, 5):
        print(players[index])

def find_player(name):
    name = name.lower()
    for player in players:
        if(name in player.lower()):
            return player
    return "No Player Found"

#Call functions
print_player_num()
print_top_five()
print(find_player("bUlBA"))