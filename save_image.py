import cv2
cap = cv2.VideoCapture(2)

while (True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    if (cv2.waitKey(1) == ord('s')):
        cv2.imwrite("cube.jpg", frame)
        print("image_saved")
    if (cv2.waitKey(1) & 0xFF == 'q'):
        break
cap.release()
cv2.destroyAllWindows()