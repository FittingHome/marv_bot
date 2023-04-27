import pyautogui
import keyboard
import time
import sys
from PIL import ImageGrab


sftp_path = "Z:\\share\\bodies"
filename = "position_souris_path.txt"
avatar_file = "position_souris_avatar.txt"

text = ' '.join(sys.argv[1:])

# Read the file and extract the x, y coordinates of each position
# # and the delay between each click
# with open(filename, "r") as f:
#     lines = f.readlines()
#     positions = [tuple(map(int, line.strip().split(","))) for line in lines[:-1]]
#     delays = list(map(int, lines[-1].strip().split(",")))

# # Click on each position with the specified delay between clicks
# for i, (x, y) in enumerate(positions):
#     pyautogui.click(x=x, y=y)
#     delay = delays[min(i, len(delays) - 1)]
#     pyautogui.PAUSE = delay

# keyboard.write(sftp_path)
# keyboard.press_and_release('enter')

# # Read the file and extract the x, y coordinates of each position
# # and the delay between each click
# with open(avatar_file, "r") as f:
#     lines = f.readlines()
#     positions = [tuple(map(int, line.strip().split(","))) for line in lines[:-1]]
#     delays = list(map(int, lines[-1].strip().split(",")))

# # Click on each position with the specified delay between clicks
# for i, (x, y) in enumerate(positions):
#     pyautogui.click(x=x, y=y)
#     delay = delays[min(i, len(delays) - 1)]
#     pyautogui.PAUSE = delay


# keyboard.write(text)
# time.sleep(2)
# keyboard.press_and_release('enter')

# time.sleep(10)
# keyboard.press_and_release('enter')
# # time.sleep(50)



image = ImageGrab.grab()
 
coordonee = x, y = 48, 1048

pixel = image.getpixel (coordonee)  #Je recupere la couleur du pixel

couleur = (62, 62, 64)
while (pixel != couleur):
        pixel = image.getpixel (coordonee)
        continue

print(pixel) 