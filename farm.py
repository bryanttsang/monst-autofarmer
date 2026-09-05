from windowcapture import Window
from imagesearch import image_search
from templates import homescreen, pick_team, ok_skip, no_stam, no_stam_ok
from constants import ORIGIN_X, ORIGIN_Y
from time import sleep

wincap = Window()

# detect if at homescreen
if not image_search(homescreen, wincap.capture(), (87, 643)):
    exit(0)

while True:
    # shortcut button
    wincap.click((300, 640), 2)

    # start quest
    while not (loc := image_search(pick_team, wincap.capture()[:,210:244])):
        if (loc := image_search(no_stam, wincap.capture(), (223, 565))):
            wincap.click((loc[0]+ORIGIN_X, loc[1]+ORIGIN_Y))
            while (loc := image_search(no_stam_ok, wincap.capture(), (226, 483))):
                wincap.click((loc[0]+ORIGIN_X, loc[1]+ORIGIN_Y))
                sleep(0.5)
        sleep(0.5)
    wincap.click((295, loc[1]+ORIGIN_Y), 5)

    # finish level
    while not (loc := image_search(ok_skip, wincap.capture(), (219, 739))):
        wincap.click((295, 567))
        wincap.drag((295, 567), (195, 470), 0.475) # 45 deg
        sleep(0.5)
    wincap.click((loc[0]+ORIGIN_X, loc[1]+ORIGIN_Y))

    # wait for homescreen
    while not image_search(homescreen, wincap.capture(), (87, 643)):
        sleep(1)
    sleep(1) # wait to fully load
