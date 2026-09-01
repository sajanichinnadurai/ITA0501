import cv2
import numpy as np

img = np.ones((500,500,3), dtype=np.uint8) * 255

text = input("Enter text: ")

cv2.putText(img, text, (80,250),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0,0,255), 2)

cv2.imshow("Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
