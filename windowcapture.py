import Quartz
from constants import NAME, SUB
import numpy as np
from time import sleep

class Window:
    id = 0

    def __init__(self):
        self.id = self.get_id()
        
    def get_id(self):
        windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListExcludeDesktopElements, Quartz.kCGNullWindowID)
        # print([w['kCGWindowName'] for w in windows])
        window = [w for w in windows if w['kCGWindowName'] in (NAME, SUB)]
        # print(window)
        return window[0]['kCGWindowNumber']

    def capture(self):
        image = Quartz.CGWindowListCreateImage(
            Quartz.CGRectMake(55, 72, 480, 788),
            Quartz.kCGWindowListOptionIncludingWindow,
            self.id,
            Quartz.kCGWindowImageBoundsIgnoreFraming | Quartz.kCGWindowImageNominalResolution
        )

        # bytes_per_row = Quartz.CGImageGetBytesPerRow(image)
        # width = Quartz.CGImageGetWidth(image)
        # height = Quartz.CGImageGetHeight(image)

        image_data_provider = Quartz.CGImageGetDataProvider(image)
        image_data = Quartz.CGDataProviderCopyData(image_data_provider)

        np_data_buffer = np.frombuffer(image_data, dtype=np.uint8)

        np_data = np_data_buffer.reshape((788, 480, 4))
        # np_data = np.lib.stride_tricks.as_strided(
        #     np_data_buffer,
        #     shape=(height, width, 3),
        #     strides=(bytes_per_row, 4, 1),
        #     writeable=False
        # )
        
        return np_data
    
    def click(self, coord: tuple, n: int = 1):
        for _ in range(n):
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, 
                Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseDown, coord, Quartz.kCGMouseButtonLeft))
            sleep(0.015)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, 
                Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseUp, coord, Quartz.kCGMouseButtonLeft))
            sleep(0.015)

    def drag(self, down: tuple, up: tuple, delay: float = 0.015):
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, 
            Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseDown, down, Quartz.kCGMouseButtonLeft))
        sleep(delay)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, 
            Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseDragged, up, Quartz.kCGMouseButtonLeft))
        sleep(0.015)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, 
            Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseUp, up, Quartz.kCGMouseButtonLeft))
        sleep(0.015)
