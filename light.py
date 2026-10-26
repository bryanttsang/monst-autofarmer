from windowcapture import Window
from imagesearch import image_search, area_search
from templates import *
from constants import *
from time import sleep, time
from datetime import datetime

# ワンワン ゼーレ コロンブス ラファエル

wincap = Window()

# detect if at homescreen
if not image_search(homescreen, wincap.capture(), HOMESCREEN_SEARCH):
    print('not at homescreen')
    exit(0)

WP_LEFT = (184, 260)
WP_TOP = (239, 205)
timer = open(f'timer/light{datetime.now().strftime("%Y%m%d%H%M")}', 'w', buffering=1, encoding='utf-8')

while True:
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

    # b1
    while not image_search(light_b2, wincap.capture(), (226, 315)):
        wincap.drag((315, 138), (145, 491))
        sleep(0.5)

    # b2
    while not image_search(light_b3, wincap.capture(), (251, 379)):
        wincap.drag((280, 138), (221, 472))
        sleep(0.5)

    # b3
    while not image_search(light_t3, wincap.capture(), (249, 627)):
        sleep(0.5)
    for _ in range(10):
        if area_search(light_wp_left, wincap.capture(), (149, 170, 272, 296)):
            wp = WP_TOP
            break
        if area_search(light_wp_top, wincap.capture(), (149, 170, 272, 296)):
            wp = WP_LEFT
            break
    for _ in range(10):
        wincap.drag(wp, (294, 482))

    # finish level
    while not (ok_skip_button := image_search(ok_skip, wincap.capture(), OKSKIP_SEARCH)):
        wincap.click((257, 470))
        wincap.drag((257, 470), (157, 370))
        sleep(0.5)
    wincap.click(ok_skip_button)

    # exit reward screen
    while not image_search(loadscreen, wincap.capture(), LOADSCREEN_SEARCH):
        wincap.click(ML_BUTTON)
        wincap.click(ok_skip_button)
        sleep(0.5)

    # mark time
    timer.write(str(time()) + '\n')

    # wait for homescreen
    while not image_search(homescreen, wincap.capture(), HOMESCREEN_SEARCH):
        sleep(0.5)
