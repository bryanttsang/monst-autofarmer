from pathlib import Path
import cv2 as cv

screenshot_folder = Path('screenshots/').glob('*.png')
template_folder = Path('templates/').glob('*.png')

screenshot_set = set([file.name for file in screenshot_folder])
template_set = set([file.name for file in template_folder])

differences = screenshot_set - template_set

for filename in differences:
    screenshot = cv.imread(f'screenshots/{filename}', cv.IMREAD_GRAYSCALE)
    converted = cv.resize(screenshot, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
    cv.imwrite(f'templates/{filename}', converted)
    print(f'Converted {filename}')
