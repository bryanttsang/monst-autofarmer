import cv2 as cv

def image_search(screen, image) -> tuple:
    result = cv.matchTemplate(cv.cvtColor(screen, cv.COLOR_BGRA2GRAY), image, cv.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv.minMaxLoc(result)

    if max_val < 0.9:
        return ()
    return max_loc
