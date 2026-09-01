import cv2

img = cv2.imread("sample.jpg")

rotate = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("270 Rotation", rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
