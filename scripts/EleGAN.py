import cv2
import numpy as np

kernel = np.ones((2,2), np.uint8) 				###Increase the (2,2) for thicker lines. 

i = 1
while i < 75:							###Depends on the number of images
	img = cv2.imread("Hack (" + str(i) + ").jpg")
	edges = 255-cv2.Canny(img, 300, 300)			###May need to change the numbers to get perfect results
	erosion = cv2.erode(edges, kernel, iterations=1) 
	cv2.imwrite("Disc_" + str(i) + ".jpg", erosion)
	i += 1

#indices = np.where(edges == [0])
