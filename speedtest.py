import cv2 as cv
from time import time
from windowcapture import Window

wincap = Window()

process_time = 0
num_loop = 600

for i in range(num_loop):
    start = time()
    screenshot = wincap.capture()
    cv.imshow('vision', screenshot)
    process_time += time() - start

    # display window capture
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('FPS:', num_loop / process_time)
