import cv2

img = cv2.imread("sample.jpg", 0)

if img is None:
    print("Image not found")
else:
    _, result = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow("Segmentation", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
