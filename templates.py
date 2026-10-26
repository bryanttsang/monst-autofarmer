from cv2 import imread, IMREAD_GRAYSCALE
from numpy import uint8

homescreen = imread("templates/homescreen.png", IMREAD_GRAYSCALE).astype(uint8)
no_stam = imread("templates/nostam.png", IMREAD_GRAYSCALE).astype(uint8)
pick_team = imread("templates/pickteam.png", IMREAD_GRAYSCALE).astype(uint8)
ok_clear = imread("templates/okclear.png", IMREAD_GRAYSCALE).astype(uint8)
ok_skip = imread("templates/okskip.png", IMREAD_GRAYSCALE).astype(uint8)
loadscreen = imread("templates/loadscreen.png", IMREAD_GRAYSCALE).astype(uint8)
