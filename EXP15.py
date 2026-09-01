import cv2

img = cv2.imread("sample.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = gray.astype("float32")

corner = cv2.cornerHarris(gray,2,3,0.04)

img[corner>0.01*corner.max()] = [0,0,255]

cv2.imshow("Corners",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
