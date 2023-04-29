#!/usr/bin/env python3

import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import time


def sensor_camera():
    
    # use a ROS subscriber to get image from the camera topic
    ros_img = rospy.wait_for_message('/camera/image_raw', Image)

    # convert from ROS Image message type to OpenCV data type
    bridge = CvBridge()
    try:
        cv_img = bridge.imgmsg_to_cv2(ros_img, "bgr8")
    except CvBridgeError as e:
        print(e)

    # convert from BGR to HSV
    hsv_img = cv.cvtColor(cv_img, cv.COLOR_BGR2HSV)

    # thresholding
    COLOR_MIN = (39, 106, 124)
    COLOR_MAX = (77, 237, 189)
    thresh_img = cv.inRange(hsv_img, COLOR_MIN, COLOR_MAX)

    cv.imshow("Thresholded HSV", thresh_img)

    cv.waitKey(1)



def main():

    # initialize ROS Node
    rospy.init_node('opencv_example')

    # set control frequency & time
    hz = 20 #hz
    rate = rospy.Rate(hz)
    t_start = time.time() # seconds

    # setup control loop
    while not rospy.is_shutdown():

        # SENSE
        sensor_camera()
        
        rate.sleep()




if __name__=='__main__':
    main()