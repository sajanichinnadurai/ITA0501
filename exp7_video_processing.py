import cv2
import time

# Read video file
cap = cv2.VideoCapture("sample.mp4")

if not cap.isOpened():
    print("Video not found!")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Normal Video
    cv2.imshow("Normal Video", frame)
    cv2.waitKey(30)

    # Slow Motion
    cv2.imshow("Slow Motion", frame)
    time.sleep(0.1)

    # Fast Motion
    cv2.imshow("Fast Motion", frame)
    cv2.waitKey(5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
