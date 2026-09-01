import cv2

# Read image in grayscale
img = cv2.imread("sample.jpg", 0)

# Check image
if img is None:
    print("Image not found!")
else:
    # Histogram Equalization
    equalized = cv2.equalizeHist(img)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Equalized Image", equalized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
