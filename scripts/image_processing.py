#! /usr/bin/env python3

import cv2 as cv
import matplotlib.pyplot as plt

def main():
    
    # read the image from directory
    img = cv.imread('front_cam_img.jpg')
    # error handling for reading file
    assert img is not None, "file could not be read"


    # convert from BGR to HSV
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # display
    cv.imshow("BGR", img)
    cv.imshow("HSV", hsv_img)

    # thresholding
    COLOR_MIN = (39, 106, 124)
    COLOR_MAX = (77, 237, 189)
    thresh_img = cv.inRange(hsv_img, COLOR_MIN, COLOR_MAX)

    cv.imshow("Thresholded HSV", thresh_img)

    # hold script till terminate key is pressed
    key = cv.waitKey(0)
    if key == ord("s"):
        cv.destroyAllWindows()


if __name__=='__main__':
    main()