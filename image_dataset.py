import os
import cv2
import numpy as np

'''
This Script is used to create and image dataset.
Upon execution of the script it will ask to select which colour's dataset you would like to create
Then align the cube faces to ROI marked in the cam feed
Press 's' to save all 9 faces to the selected folder
'''
cap = cv2.VideoCapture(2)

Face_cordintes = np.array([[(180, 110), (240, 165)], [(270, 110), (330, 165)], [(360, 110), (420, 165)],
                           [(190, 195), (250, 250)], [(275, 195), (335, 250)], [(360, 195), (420, 250)],
                           [(195, 280), (250, 325)], [(280, 280), (330, 325)], [(360, 280), (410, 325)]])

Faces = np.array(([np.zeros((55, 60, 3)), np.zeros((55, 60, 3)), np.zeros((55, 60, 3)),
                   np.zeros((55, 60, 3)), np.zeros((55, 60, 3)), np.zeros((55, 60, 3)),
                   np.zeros((45, 55, 3)), np.zeros((45, 50, 3)), np.zeros((45, 50, 3))]), dtype=object)


j = 0


colour = input("Select Colour r/g/b/o/y/w:")
i = 0
while (True):
    _, frame = cap.read()
    frame_copy = frame
    i = 0
    for cordinates in Face_cordintes:
        point1 = tuple(cordinates[0])
        point2 = tuple(cordinates[1])
        cv2.rectangle(frame, point1, point2, (255, 255, 255), 2)

        x_len = abs(cordinates[0, 0] - cordinates[1, 0])
        y_len = abs(cordinates[0, 1] - cordinates[1, 1])

        Faces[i] = frame_copy[cordinates[0, 1]:cordinates[1, 1], cordinates[0, 0]:cordinates[1, 0]]
        i += 1

    '''cv2.rectangle(frame, (180, 110), (240, 165), (255, 255, 255), 2)
    cv2.rectangle(frame, (270, 110), (330, 165), (255, 255, 255), 2)
    cv2.rectangle(frame, (360, 110), (420, 165), (255, 255, 255), 2)

    cv2.rectangle(frame, (190, 195), (250, 250), (255, 255, 255), 2)
    cv2.rectangle(frame, (275, 195), (335, 250), (255, 255, 255), 2)
    cv2.rectangle(frame, (360, 195), (420, 250), (255, 255, 255), 2)

    cv2.rectangle(frame, (195, 280), (250, 325), (255, 255, 255), 2)
    cv2.rectangle(frame, (280, 280), (330, 325), (255, 255, 255), 2)
    cv2.rectangle(frame, (360, 280), (410, 325), (255, 255, 255), 2)'''

    # cropped = frame[110:165, 180:240]
    # print(cropped)
    # cv2.imshow("cropped", cropped)

    cv2.imshow("img", frame)
    # cv2.imshow("face1", Faces[8])

    if (cv2.waitKey(1) == ord('s')):
        for face in Faces:
            path = os.path.join("./Dataset/Test", colour)
            filename = os.path.join(path, str(j) + ".jpg")
            print(filename)
            cv2.imwrite(filename, face)
            j += 1
            print("Image Saved")

    if (cv2.waitKey(1) & 0xFF == 'q'):
        break

cap.release()
cv2.destroyAllWindows()