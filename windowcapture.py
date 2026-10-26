# type: ignore[attr-defined]
import Quartz
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from numpy import frombuffer, uint8
from time import sleep

screen_bounds = Quartz.CGRectMake(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
list_option = Quartz.kCGWindowListOptionOnScreenOnly
window_ID = Quartz.kCGNullWindowID
image_option = Quartz.kCGWindowImageBoundsIgnoreFraming | Quartz.kCGWindowImageNominalResolution
_CGWindowListCreateImage = Quartz.CGWindowListCreateImage
_CGDataProviderCopyData = Quartz.CGDataProviderCopyData
_CGImageGetDataProvider = Quartz.CGImageGetDataProvider

kCGHIDEventTap = Quartz.kCGHIDEventTap
kCGEventLeftMouseDown = Quartz.kCGEventLeftMouseDown
kCGEventLeftMouseUp = Quartz.kCGEventLeftMouseUp
kCGEventLeftMouseDragged = Quartz.kCGEventLeftMouseDragged
kCGMouseButtonLeft = Quartz.kCGMouseButtonLeft
_CGEventPost = Quartz.CGEventPost
_CGEventCreateMouseEvent = Quartz.CGEventCreateMouseEvent

class Window:
    def capture(self):
        image = _CGWindowListCreateImage(screen_bounds, list_option, window_ID, image_option)
        image_data = _CGDataProviderCopyData(_CGImageGetDataProvider(image))
        return frombuffer(image_data, dtype=uint8).reshape((WINDOW_HEIGHT, WINDOW_WIDTH, 4))
    
    def click(self, coord: tuple, n: int = 1):
        for _ in range(n):
            _CGEventPost(kCGHIDEventTap, 
                _CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, coord, kCGMouseButtonLeft))
            sleep(0.015)
            _CGEventPost(kCGHIDEventTap, 
                _CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, coord, kCGMouseButtonLeft))
            sleep(0.015)

    def drag(self, down: tuple, up: tuple, delay: float = 0.015):
        _CGEventPost(kCGHIDEventTap, 
            _CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, down, kCGMouseButtonLeft))
        sleep(delay)
        _CGEventPost(kCGHIDEventTap, 
            _CGEventCreateMouseEvent(None, kCGEventLeftMouseDragged, up, kCGMouseButtonLeft))
        sleep(0.015)
        _CGEventPost(kCGHIDEventTap, 
            _CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, up, kCGMouseButtonLeft))
        sleep(0.015)
