#! /usr/bin/env python3

import cv2 as cv
from cv_bridge import CvBridge, CvBridgeError
import matplotlib.pyplot as plt

def main():
    
    # read the image from directory
    img = cv.imread('front_cam_img.jpg')
    # error handling for reading file
    assert img is not None, "file could not be read"

    # Inspect data type
    print('OpenCV image data type:', type(img))

    # Image data shape
    print(f'Image data shape: {img.shape}')

    # Split image data into channels
    channels = cv.split(img)
    titles = ['Original Image', 'Blue', 'Green', 'Red']

    # plot the channels
    plt.subplot(1,4,1)
    plt.imshow(img, 'gray'), plt.title(titles[0])

    for i in range(len(channels)):
        plt.subplot(1,4,i+2)
        plt.imshow(channels[i], 'gray')
        plt.title(titles[i+1])

    plt.show()

    # hold script till terminate key is pressed
    key = cv.waitKey(0)
    if key == ord("s"):
        cv.destroyAllWindows()


if __name__=='__main__':
    main()