from numpy import uint8
from numpy.typing import NDArray
import cv2 as cv

def image_search(template: NDArray[uint8], screen: NDArray[uint8], coord: tuple = ()) -> tuple:
    """
    Search whether a template is visible on the screen (at coord if provided)
    Return the coord of the template if found
    """

    if coord:
        x, y = coord
        h, w = template.shape
        screen = screen[y:y+h, x:x+w]
    
    result = cv.matchTemplate(cv.cvtColor(screen, cv.COLOR_BGRA2GRAY), template, cv.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv.minMaxLoc(result)
    
    # cv.imwrite('test/image_search.png', screen)
    # print(max_loc, max_val)

    return coord or tuple(max_loc) if max_val >= 0.9 else ()

def area_search(template: NDArray[uint8], screen: NDArray[uint8], coord: tuple) -> tuple:
    """
    Search whether a template is visible on the screen within the provided area
    Return the coord of the template if found
    """
    
    x0, y0, x1, y1 = coord
    screen = screen[y0:y1, x0:x1]
    
    result = cv.matchTemplate(cv.cvtColor(screen, cv.COLOR_BGRA2GRAY), template, cv.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv.minMaxLoc(result)

    # cv.imwrite('test/area_search.png', screen)
    # print(max_loc, max_val)

    return (max_loc[0]+x0, max_loc[1]+y0) if max_val >= 0.9 else ()
