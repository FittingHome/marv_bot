import sys
import sys
from pynput import mouse, keyboard

filename = "position_sourisv2.txt"

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        with open(filename, "a") as f:
            f.write(f"Souris cliquée à la position ({x}, {y})\n")
            f.close()

with mouse.Listener(on_click=on_click) as listener1:
    listener1.join()

#import pyautogui
#
## Fonction pour récupérer la position de la souris lors d'un clic
#def on_click(x, y, button, pressed):
#    pass  # Ne fait rien
#
## Nom du fichier texte contenant les positions et les délais
#filename = "positions_clics.txt"
#
## Lecture des positions et des délais à partir du fichier texte
#positions = []
#delais = []
#with open(filename, "r") as f:
#    for line in f:
#        values = line.strip().split(",")
#        x, y = map(int, values[:2])
#        positions.append((x, y))
#        if len(values) > 2:
#            delai = float(values[2])
#            delais.append(delai)
#
## Clic sur toutes les positions avec les délais spécifiés
#for i, pos in enumerate(positions):
#    pyautogui.click(pos)
#    if i < len(delais):