import numpy as np
import cv2

cap = cv2.VideoCapture(2)
def applyKernel(b_frame, g_frame, r_frame):
    kernel = np.array( [[0, -0.7, 0], [-0.7, 5, -0.7], [0, -0.7, 0]] )
    b_frame = cv2.filter2D(b_frame, -1, kernel)
    g_frame = cv2.filter2D(g_frame, -1, kernel)
    r_frame = cv2.filter2D(r_frame, -1, kernel)

    img = cv2.merge((b_frame, g_frame, r_frame))
    return img

def findfaces(edge):
    _, contours, _ = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)
    closed_cont = []
    for cont in contours:
        if (cv2.isContourConvex(cont) == True):
            closed_cont.append(cont)
    return closed_cont

while (True):
    ret, frame = cap.read()

    b_frame, g_frame, r_frame = cv2.split(frame)
    img = applyKernel(b_frame, g_frame, r_frame)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(img, 110, 250, cv2.THRESH_BINARY)
    edge = cv2.Canny(img, 230, 300, apertureSize=3)

    cv2.imshow("img", img)
    cv2.imshow("threshed", thresh)

    contour = findfaces(edge)
    #cv2.drawContours(frame, contour, -1, (255, 255, 60), thickness=1)
    #cv2.imshow("frame", frame)

    if (cv2.waitKey(1) & 0xFF == 'q'):
        break

cap.release()
cv2.destroyAllWindows()
