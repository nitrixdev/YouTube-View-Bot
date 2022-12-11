from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import random
import string
import colorama
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import threading, requests, ctypes, os, time, random, string
from datetime import datetime
from colorama import Fore, Style
from random import *

PATH = "chromedriver.exe"

amount = 0
error = 0

os.system(f"title Youtube View Bot ^| Views: {amount} ^| Errors: {error}")

os.system("cls")

url = input("> Enter Video URL: ")
count = input("> Enter View Count: ")

delay = int(input("> Enter Watch Time (seconds): "))

driver = webdriver.Chrome(PATH)


while count == count:
    driver.minimize_window()
    os.system(f"title Youtube View Bot ^| Views: {amount} ^| Errors: {error}")
    driver.get(url)
    time.sleep(delay)
    amount += 1
    driver.refresh()
