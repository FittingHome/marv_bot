import pyautogui

filename = "positionv2_souris.txt"

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
