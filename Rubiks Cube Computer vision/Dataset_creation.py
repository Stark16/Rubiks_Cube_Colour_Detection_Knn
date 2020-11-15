import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

'''
1. Reads the images on the respective folders taking folder names as labels
2. saves the corresponding Image's hue and saturation values with it;s colour as lable in a text file
'''

fh = open("./Dataset/Complete_data.txt", 'w')


def save_data(hist_hue, hist_sat, Clr):

    data = [hist_hue, hist_sat, Clr]
    fh.write(str(hist_hue) + ',' + str(hist_sat) + ',' + Clr + ",\n")

def histogram_cal(hsv, Clr):
    if Clr == 'r':
        colour = 'red'
    elif Clr == 'b':
        colour = 'blue'
    elif Clr == 'g':
        colour = 'green'
    elif Clr == 'y':
        colour = 'yellow'
    elif Clr == 'w':
        colour = 'grey'
    elif Clr == 'o':
        colour = 'orange'

    hue = hsv[..., 0].flatten()
    sat = hsv[..., 1].flatten()

    hist_hue = np.histogram(hue, bins=np.arange(256))
    hist_sat = np.histogram(sat, bins=np.arange(256))

    h = np.argmax(hist_hue[0])
    s = np.argmax(hist_sat[0])

    plt.scatter(h, s, color=colour)

    save_data(h, s, Clr)


for folder in os.listdir("./Dataset/Train"):
    Clr = str(folder)
    for img in os.listdir(os.path.join("./Dataset/Train", str(folder))):
        path = os.path.join("./Dataset/Train", str(folder), str(img))

        pixel = cv2.imread(path)

        hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)

        histogram_cal(hsv, Clr)

plt.show()
fh.close()
