from pathlib import Path
import cv2 as cv

screenshot_folder = Path('screenshots/')
template_folder = Path('templates/')

for src_path in screenshot_folder.rglob('*.png'):
    screenshot_path = src_path.relative_to(screenshot_folder)
    template_path = template_folder / screenshot_path

    if not template_path.exists():
        template_path.parent.mkdir(parents=True, exist_ok=True)
        screenshot = cv.imread(str(src_path), cv.IMREAD_GRAYSCALE)
        cv.imwrite(str(template_path), screenshot)
        print(f'Converted {str(screenshot_path)}')
