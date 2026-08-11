import cv2
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Original", image)
#cv2.imshow("Grayscale", gray)

img = cv2.imread("img.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()