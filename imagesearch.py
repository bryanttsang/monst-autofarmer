from numpy import uint8
from numpy.typing import NDArray
import cv2 as cv

def image_search(template: NDArray[uint8], screen: NDArray[uint8], origin: tuple = ()) -> tuple:
    """
    Search whether a template is visible on the screen
    Use the whole screen if origin (top left pixel coord) is not provided
    Return the coord of the template if found
    """

    if origin:
        x, y = origin
        h, w = template.shape
        screen = screen[y:y+h, x:x+w]
    
    result = cv.matchTemplate(cv.cvtColor(screen, cv.COLOR_BGRA2GRAY), template, cv.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv.minMaxLoc(result)

    # cv.imwrite('test/a.png', screen)
    # print(max_val, max_loc)

    if max_val < 0.9:
        return ()
    
    if origin:
        return (max_loc[0]+x, max_loc[1]+y)
    
    return max_loc
