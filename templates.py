from cv2 import imread, IMREAD_GRAYSCALE
from numpy import uint8

homescreen = imread("templates/homescreen.png", IMREAD_GRAYSCALE).astype(uint8)
no_stam = imread("templates/nostam.png", IMREAD_GRAYSCALE).astype(uint8)
pick_team = imread("templates/pickteam.png", IMREAD_GRAYSCALE).astype(uint8)
ok_clear = imread("templates/okclear.png", IMREAD_GRAYSCALE).astype(uint8)
ok_skip = imread("templates/okskip.png", IMREAD_GRAYSCALE).astype(uint8)
loadscreen = imread("templates/loadscreen.png", IMREAD_GRAYSCALE).astype(uint8)

fire_b2 = imread("templates/fire/b2.png", IMREAD_GRAYSCALE).astype(uint8)
fire_b3 = imread("templates/fire/b3.png", IMREAD_GRAYSCALE).astype(uint8)

light_b2 = imread("templates/light/b2.png", IMREAD_GRAYSCALE).astype(uint8)
light_b3 = imread("templates/light/b3.png", IMREAD_GRAYSCALE).astype(uint8)
light_t3 = imread("templates/light/t3.png", IMREAD_GRAYSCALE).astype(uint8)
light_wp_left = imread("templates/light/wp_left.png", IMREAD_GRAYSCALE).astype(uint8)
light_wp_top = imread("templates/light/wp_top.png", IMREAD_GRAYSCALE).astype(uint8)
