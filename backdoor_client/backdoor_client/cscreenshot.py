"""
Reference:
1) https://www.askpython.com/python/examples/capture-screenshots
"""
from PIL import ImageGrab

ss_region = (0, 0, 1920, 920)
ss_image = ImageGrab.grab(ss_region)
ss_image.save("image.jpg")
