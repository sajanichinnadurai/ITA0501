import cv2
img = cv2.imread('sample.jpg')
cv2.imshow('Original', img)
cv2.imshow('Blur', cv2.GaussianBlur(img, (5, 5), 0))
cv2.waitKey(0)
cv2.destroyAllWindows()