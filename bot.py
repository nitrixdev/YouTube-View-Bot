import undetected_chromedriver as uc
import time, os
from colorama import Fore, Back, Style

os.system("title View Bot V1 ^| Success: 0")

url = input("> Enter Video Link: ")
views = input("> Enter Amount Of Views: "))
delay = int(input("> Enter Watchtime: "))

count = 0

uc.install(
    executable_path='c:/users/user1/chromedriver.exe',
)

print(f"""{Fore.RED}
        _               _           _   
 __   _(_) _____      _| |__   ___ | |_ 
 \ \ / / |/ _ \ \ /\ / / '_ \ / _ \| __|
  \ V /| |  __/\ V  V /| |_) | (_) | |_ 
   \_/ |_|\___| \_/\_/ |_.__/ \___/ \__|
                                        """)

opts = uc.ChromeOptions()
driver = uc.Chrome(options=opts)
for i in range(views): 
    os.system(f"title View Bot V1 ^| Success: {count}")
    driver.get(url)
    time.sleep(delay)
    driver.refresh()
    print(f"{Fore.GREEN}Sent view!")
    count += 1
    
print(f"{Fore.YELLOW}Done!")
