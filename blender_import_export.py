import pyautogui
import pyperclip
import keyboard
import time
import sys
import subprocess

import_path = "J:\\EPITECH\\Export_fbx"

#export_path = ""

process = "blender_app.txt"

blender_import_path = "blender_import_path.txt"
blender_import_filename = "blender_import_filename.txt"
blender_import = "blender_import.txt"

blender_file = "position_sourisv2.txt"
# blender_export_path = ""
# blender_export_filename = ""
# blender_export = """

blender_filename = ' '.join(sys.argv[1:])

#avatar_file = "position_souris_avatar.txt"

# Read the file and extract the x, y coordinates of each position
# and the delay between each click
with open(process, "r") as f:
    lines = f.readlines()
    positions = [tuple(map(int, line.strip().split(","))) for line in lines[:-1]]
    delays = list(map(int, lines[-1].strip().split(",")))

# Click on each position with the specified delay between clicks
for i, (x, y) in enumerate(positions):
    pyautogui.click(x=x, y=y)
    delay = delays[min(i, len(delays) - 1)]
    pyautogui.PAUSE = delay

keyboard.press_and_release('a')
keyboard.press_and_release('x')
keyboard.press_and_release('enter')

time.sleep(1)
keyboard.press_and_release('q')
keyboard.press_and_release('down')
keyboard.press_and_release('enter')
time.sleep(1)

with open(blender_import_path, "r") as f:
    lines = f.readlines()
    pos3 = [tuple(map(int, line.strip().split(","))) for line in lines[:-1]]
    delays = list(map(int, lines[-1].strip().split(",")))

# Click on each position with the specified delay between clicks
for i, (x, y) in enumerate(pos3):
    pyautogui.click(x=x, y=y)
    pyautogui.click(x=x, y=y)

    delay = delays[min(i, len(delays) - 1)]
    pyautogui.PAUSE = delay

keyboard.write("hello")
keyboard.press_and_release('enter')
# Read the file and extract the x, y coordinates of each position
# and the delay between each click
with open(blender_import_filename, "r") as f:
    lines = f.readlines()
    pos2 = [tuple(map(int, line.strip().split(","))) for line in lines[:-1]]
    delays = list(map(int, lines[-1].strip().split(",")))

# Click on each position with the specified delay between clicks
for i, (x, y) in enumerate(pos2):
    pyautogui.click(x=x, y=y)
    delay = delays[min(i, len(delays) - 1)]
    pyautogui.PAUSE = delay

pyperclip.copy(blender_filename)
a = pyperclip.paste()
print(a)
#keyboard.write(blender_filename)
time.sleep(2)

# # Read the file and extract the x, y coordinates of each position
# # and the delay between each click
with open(blender_import, "r") as f:
    lines = f.readlines()
    pos1 = [tuple(map(int, line.strip().split(","))) for line in lines[:-1]]
    delays = list(map(int, lines[-1].strip().split(",")))

# Click on each position with the specified delay between clicks
for i, (x, y) in enumerate(pos1):
    pyautogui.click(x=x, y=y)
    pyautogui.click(x=x, y=y)
    delay = delays[min(i, len(delays) - 1)]
    pyautogui.PAUSE = delay


# keyboard.press_and_release('enter')
# time.sleep(10)
with open(blender_file, "r") as f:
    lines = f.readlines()
    pos1 = [tuple(map(int, line.strip().split(","))) for line in lines[:-1]]
    delays = list(map(int, lines[-1].strip().split(",")))

# Click on each position with the specified delay between clicks
for i, (x, y) in enumerate(pos1):
    pyautogui.click(x=x, y=y)
    pyautogui.click(x=x, y=y)
    delay = delays[min(i, len(delays) - 1)]
    pyautogui.PAUSE = delay

keyboard.write("hello")