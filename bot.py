from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, os
from colorama import Fore, Back, Style

os.system("start https://discord.gg/45u5Amnpqp")

print(f"""{Fore.RED}
        _               _           _   
 __   _(_) _____      _| |__   ___ | |_ 
 \ \ / / |/ _ \ \ /\ / / '_ \ / _ \| __|
  \ V /| |  __/\ V  V /| |_) | (_) | |_ 
   \_/ |_|\___| \_/\_/ |_.__/ \___/ \__|
                                        """)

os.system("title View Bot V1 ^| Success: 0")

URL = input("> Enter Video Link: ")

count = 0

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

DRIVERS = 5
driver = []
BreakRate = 10 #sec
PATH = 'chromedriver.exe' #path of chromedriver

for i in range(DRIVERS):
    driver.append(webdriver.Chrome(PATH))
    driver.minimize_window()  
    driver[i].get(URL)
    action = ActionChains(driver[i])
    action.send_keys(Keys.SPACE)
    action.perform()
    os.system(f"title View Bot V1 ^| Success: {str(count)}")
        
while True:
    time.sleep(BreakRate)
    for j in range(DRIVERS):
        driver.minimize_window() 
        driver[j].refresh()
        action = ActionChains(driver[j])
        action.send_keys(Keys.SPACE)
        action.perform()
        count += 1
        os.system(f"title View Bot V1 ^| Success: {str(count)}")
