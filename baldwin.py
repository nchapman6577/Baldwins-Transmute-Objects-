import pyautogui
import time
import math
import random

ADD_FILE_LOC = "add.png"
COLLECT_FILE_LOC = "collect.png"
ITEM_FILE_LOC = "item.png"
MATERIALS_FILE_LOC = "materials.png"
TRANSMUTE_FILE_LOC = "transmute.png"
STARTPLUS_FILE_LOC = "startplus.png"
CANCEL_FILE_LOC = "cancel.png"

NUM_LOOPS = 100 # The maximum number of games we'll play. After this number, the script will quit.

i = 1
while(i < NUM_LOOPS):
    print("Start Brew:")
    print(i)
    pyautogui.click(#start button/ plus button/ first transmute button
			pyautogui.locateOnScreen(
                STARTPLUS_FILE_LOC
                )
        )
    print("Clicked plus button")
    time.sleep(random.randint(0,9))
    
    pyautogui.click(x=random.randint(320,650),y=random.randint(502,510))
    print("Clicked FMAFO button")
    time.sleep(random.randint(0,9))#Food | Materials | Apparel | Familiars | Other
    
    pyautogui.click(x=random.randint(250,275),y=random.randint(550,575))
    print("Clicked item button")
    time.sleep(random.randint(0,9))
    
    pyautogui.click(
			pyautogui.locateOnScreen(
                ADD_FILE_LOC
                )
        )
    print("Clicked add button")
    time.sleep(random.randint(0,9))
    
    pyautogui.click(
			pyautogui.locateOnScreen(
                TRANSMUTE_FILE_LOC
                )
        )
    print("Clicked transmute button and now waiting")
    time.sleep(random.randint(1860,1980))
    print("Time up")
    pyautogui.click(
			pyautogui.locateOnScreen(
                COLLECT_FILE_LOC
                )
        )
    print("Clicked collect button")
    time.sleep(random.randint(0,9))
    print("End Brew:")
    print(i)
    print("----------------------------------")
    i += 1
    

    