from windowcapture import Window
from imagesearch import image_search
from templates import homescreen, pick_team, ok_skip
from constants import ORIGIN_X, ORIGIN_Y
from time import sleep

wincap = Window()

# detect if at homescreen
if not image_search(homescreen, wincap.capture(), (87, 611)):
    exit(0)

while True:
    # shortcut button
    wincap.click((300, 640), 2)

    # start quest
    while not (loc := image_search(pick_team, wincap.capture()[:,210:244])):
        sleep(0.5)
    wincap.click((295, loc[1]+ORIGIN_Y), 5)

    # finish level
    while not (loc := image_search(ok_skip, wincap.capture(), (219, 739))):
        wincap.click((295, 567))
        wincap.drag((295, 567), (195, 470)) # 45 deg
        sleep(0.5)
    wincap.click((loc[0]+ORIGIN_X, loc[1]+ORIGIN_Y))

    # wait for homescreen
    while not image_search(homescreen, wincap.capture(), (87, 611)):
        sleep(1)
    sleep(1) # wait to fully load
