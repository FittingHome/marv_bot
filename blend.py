import pyautogui
import keyboard
import time
import sys
import os
import re
import shutil

blender_script = ' '.join(sys.argv[1:])

process = "blender_app.txt"
script = "position_sourisse.txt"
script2 = "position_sourisse2.txt"
path_import = "J:\\\\EPITECH\\\\Export_fbx\\\\" + blender_script

path_export = "J:\\\\EPITECH\\\\Export_fbx\\\\export\\\\" + blender_script

_export = "J:\EPITECH\Export_fbx\export\\" + blender_script


sftp_path = "Z:\share\\bodies"

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


f = open("J:\\blender_script\\script.py", "a")
f.truncate(0)
f.write("import bpy\n\nbpy.ops.import_scene.fbx(filepath=\'")
f.write(path_import)
f.write("\')")
f.close()

with open(script, "r") as f:
    lines = f.readlines()
    positions = [tuple(map(int, line.strip().split(","))) for line in lines[:-1]]
    delays = list(map(int, lines[-1].strip().split(",")))

# Click on each position with the specified delay between clicks
for i, (x, y) in enumerate(positions):
    pyautogui.click(x=x, y=y)
    delay = delays[min(i, len(delays) - 1)]
    pyautogui.PAUSE = delay


time.sleep(10)


f = open("J:\\blender_script\\script.py", "a")
f.truncate(0)
f.write("import bpy\n\nbpy.ops.export_scene.fbx(filepath=\'")
f.write(path_export)
f.write("\', use_selection=True)")
f.close()


with open(script2, "r") as f:
    lines = f.readlines()
    positions = [tuple(map(int, line.strip().split(","))) for line in lines[:-1]]
    delays = list(map(int, lines[-1].strip().split(",")))

# Click on each position with the specified delay between clicks
for i, (x, y) in enumerate(positions):
    pyautogui.click(x=x, y=y)
    pyautogui.click(x=x, y=y)
    delay = delays[min(i, len(delays) - 1)]
    pyautogui.PAUSE = delay

with open(script, "r") as f:
    lines = f.readlines()
    positions = [tuple(map(int, line.strip().split(","))) for line in lines[:-1]]
    delays = list(map(int, lines[-1].strip().split(",")))

# Click on each position with the specified delay between clicks
for i, (x, y) in enumerate(positions):
    pyautogui.click(x=x, y=y)
    delay = delays[min(i, len(delays) - 1)]
    pyautogui.PAUSE = delay

shutil.move(_export, sftp_path)
