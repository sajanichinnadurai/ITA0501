import cv2

# Read image
img = cv2.imread("sample.jpg")

# Check image
if img is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Gray Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
