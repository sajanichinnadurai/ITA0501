import cv2

# Read image
img = cv2.imread("sample.jpg")

# Check image
if img is None:
    print("Image not found!")
else:
    # Rotate 90 degrees clockwise
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("90 Degree Rotated Image", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
