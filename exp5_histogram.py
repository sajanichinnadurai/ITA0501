import cv2

# Read image
img = cv2.imread("sample.jpg")

# Check image
if img is None:
    print("Image not found!")
else:
    # Calculate histogram for Blue, Green and Red channels
    hist_b = cv2.calcHist([img], [0], None, [256], [0,256])
    hist_g = cv2.calcHist([img], [1], None, [256], [0,256])
    hist_r = cv2.calcHist([img], [2], None, [256], [0,256])

    print("Blue Histogram:")
    print(hist_b)

    print("Green Histogram:")
    print(hist_g)

    print("Red Histogram:")
    print(hist_r)

    cv2.imshow("Original Image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
