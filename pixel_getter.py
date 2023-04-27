from PIL import ImageGrab

image = ImageGrab.grab()
 
coordonee = x, y = 248, 1055
pixel = image.getpixel (coordonee)  #Je recupere la couleur du pixel
 
print(pixel) 