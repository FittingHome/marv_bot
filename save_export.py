import pyautogui
import keyboard
import time
import sys

export_path = "J:\EPITECH\Export_fbx"
filename = "positionv2_souris.txt"
avatar_file = "position_souris_export.txt"
accept = "position_souris_accept.txt"

text = ' '.join(sys.argv[1:])

# Read the file and extract the x, y coordinates of each position
# and the delay between each click
with open(filename, "r") as f:
    lines = f.readlines()
    positions = [tuple(map(int, line.strip().split(","))) for line in lines[:-1]]
    delays = list(map(int, lines[-1].strip().split(",")))

# Click on each position with the specified delay between clicks
for i, (x, y) in enumerate(positions):
    pyautogui.click(x=x, y=y)
    delay = delays[min(i, len(delays) - 1)]
    pyautogui.PAUSE = delay

keyboard.write(export_path)
keyboard.press_and_release('enter')

# Read the file and extract the x, y coordinates of each position
# and the delay between each click
with open(avatar_file, "r") as f:
    lines = f.readlines()
    positions = [tuple(map(int, line.strip().split(","))) for line in lines[:-1]]
    delays = list(map(int, lines[-1].strip().split(",")))

# Click on each position with the specified delay between clicks
for i, (x, y) in enumerate(positions):
    pyautogui.click(x=x, y=y)
    delay = delays[min(i, len(delays) - 1)]
    pyautogui.PAUSE = delay


keyboard.write(text)
time.sleep(2)
keyboard.press_and_release('enter')


time.sleep(3)
# Read the file and extract the x, y coordinates of each position
# and the delay between each click
with open(accept, "r") as f:
    lines = f.readlines()
    positions = [tuple(map(int, line.strip().split(","))) for line in lines[:-1]]
    delays = list(map(int, lines[-1].strip().split(",")))

# Click on each position with the specified delay between clicks
for i, (x, y) in enumerate(positions):
    pyautogui.click(x=x, y=y)
    delay = delays[min(i, len(delays) - 1)]
    pyautogui.PAUSE = delay


##ici faire une fonction qui permet d'attendre la fin de l'export en verifiant l'etat du pixel
time.sleep(20)
