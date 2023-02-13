"""
Reference:
1) https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
"""
from installer import install

try:
	import pygame
	import pygame.camera
except:
	install('pygame')

pygame.camera.init()
camlist = pygame.camera.list_cameras()

if camlist:
	cam = pygame.camera.Camera(camlist[0], (640, 480))
	cam.start()
	image = cam.get_image()
	pygame.image.save(image, "image.jpg")
else:
	print("No camera on current device")
