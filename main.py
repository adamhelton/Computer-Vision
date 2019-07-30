import cv2

img = cv2.imread("718_1000.jpg", 1)


resized_image = cv2.resize(img,(1000,500))
cv2.imshow("718_1000", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()