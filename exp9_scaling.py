import cv2

# Read image
img = cv2.imread("sample.jpg")

# Check image
if img is None:
    print("Image not found!")
else:
    # Resize to smaller size
    small = cv2.resize(img, (300, 200))

    # Resize to bigger size
    big = cv2.resize(img, (800, 600))

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Smaller Image", small)
    cv2.imshow("Bigger Image", big)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
