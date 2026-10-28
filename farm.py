from windowcapture import Window
from imagesearch import image_search, area_search
from templates import *
from constants import *
from time import sleep, time
from datetime import datetime

wincap = Window()

# detect if at homescreen
if not image_search(homescreen, wincap.capture(), HOMESCREEN_SEARCH):
    print('not at homescreen')
    exit(0)

timer = open(f'timer/farm{datetime.now().strftime("%Y%m%d%H%M")}', 'w', buffering=1, encoding='utf-8')

while True:
    # shortcut button
    wincap.click(SHORTCUT_BUTTON, 2)

    # start quest
    while not (start_quest_button := area_search(pick_team, wincap.capture(), PICKTEAM_SEARCH)):
        # no stam
        if no_stam_button := area_search(no_stam, wincap.capture(), NOSTAM_SEARCH):
            wincap.click(no_stam_button)
            while not (start_quest_button := area_search(pick_team, wincap.capture(), PICKTEAM_SEARCH)):
                wincap.click(NOSTAMOK_BUTTON, 2)
                sleep(0.5)
            break

        # stam spark
        if image_search(homescreen, wincap.capture(), HOMESCREEN_SEARCH):
            wincap.click(SHORTCUT_BUTTON, 2)
        
        sleep(0.5)
    wincap.click(start_quest_button, 10)

    # finish level
    while not (ok_skip_button := image_search(ok_skip, wincap.capture(), OKSKIP_SEARCH)):
        wincap.click(STAGECLEAR_BUTTON)
        wincap.drag(STAGECLEAR_BUTTON, (157, 370), 0.475) # 45 deg
        # wincap.drag(STAGECLEAR_BUTTON, (157, 370)) # no gauge
        wincap.click(CONNECTIONERROR_BUTTON)
        wincap.click(CONNECTIONRETRY_BUTTON)
        sleep(0.5)
    wincap.click(ok_skip_button)

    # exit reward screen
    while not image_search(loadscreen, wincap.capture(), LOADSCREEN_SEARCH):
        wincap.click(ML_BUTTON)
        # TODO: ex decline button
        wincap.click(ok_skip_button)
        sleep(0.5)
    
    # mark time
    timer.write(str(time()) + '\n')

    # wait for homescreen
    while not image_search(homescreen, wincap.capture(), HOMESCREEN_SEARCH):
        sleep(0.5)
