# finding lanes on the road

import cv2
import numpy as np
import matplotlib.pyplot as plt

# canny edge detection
def canny(image):

	# Convert image to GrayScale
	gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

	# Reduce Noise, convolving with a blur of 5x5 kernel
	blur = cv2.GaussianBlur(gray, (5, 5), 0)

	# Apply Canny function
	canny = cv2.Canny(blur, 50, 150)

	return canny

# Region of Interest
def region_of_interest(image):
	height = image.shape[0]
	polygons = np.array([[(200, height), (1100, height), (550, 250)]])
	mask = np.zeros_like(image)
	cv2.fillPoly(mask, polygons, 255)
	
	# bitwise and(&) with all 1's has no effect
	masked_image = cv2.bitwise_and(image, mask)

	return masked_image

image = cv2.imread('2.1_test_image.jpg')
# print (type(image))
lane_image = np.copy(image)
canny_image = canny(lane_image)
cropped_image = region_of_interest(canny_image)

# show image
cv2.imshow('result', cropped_image)
cv2.waitKey(0)