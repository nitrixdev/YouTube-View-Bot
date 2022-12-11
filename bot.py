from selenium import webdriver
import time, os
from colorama import Fore, Back, Style


print(f"""{Fore.RED}
        _               _           _   
 __   _(_) _____      _| |__   ___ | |_ 
 \ \ / / |/ _ \ \ /\ / / '_ \ / _ \| __|
  \ V /| |  __/\ V  V /| |_) | (_) | |_ 
   \_/ |_|\___| \_/\_/ |_.__/ \___/ \__|
                                        """)

os.system("title View Bot V1 ^| Success: 0")

url = input("> Enter Video Link: ")
views = input("> Enter Amount Of Views: ")
delay = int(input("> Enter Watchtime: "))

count = 0

opts = uc.ChromeOptions()
driver = uc.Chrome(options=opts)
for i in range(views): 
    os.system(f"title View Bot V1 ^| Success: {str(count)}")
    siddharth3.get("https://youtu.be/OU69JaZ1FQo")
    time.sleep(delay)
    siddharth3.refresh()
    print(f"{Fore.GREEN}Sent view!")
    count += 1
    
print(f"{Fore.YELLOW}Done!")
