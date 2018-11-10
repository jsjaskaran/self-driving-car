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


image = cv2.imread('2.1_test_image.jpg')
# print (type(image))
lane_image = np.copy(image)
canny_image = canny(lane_image)

# show image
cv2.imshow('result', canny_image)
cv2.waitKey(0)