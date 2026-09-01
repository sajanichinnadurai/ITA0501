import cv2

# Read image
img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found")
else:
    # Crop ROI
    roi = img[50:200, 50:200]

    # Get ROI size
    h, w = roi.shape[:2]

    # Paste ROI at a safe position
    x = 10
    y = 10

    img[y:y+h, x:x+w] = roi

    # Display result
    cv2.imshow("ROI Copy and Paste", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
