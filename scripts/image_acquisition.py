#!/usr/bin/env python3

import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def main():
  
    # intialize the ROS node
    rospy.init_node('image_converter', anonymous=True)

    # use a ROS subscriber to get image from the camera topic
    ros_img = rospy.wait_for_message('/camera/image_raw', Image)

    # convert from ROS Image message type to OpenCV data type
    bridge = CvBridge()
    try:
        cv_img = bridge.imgmsg_to_cv2(ros_img, "bgr8")
    except CvBridgeError as e:
        print(e)

    # display image in window
    cv.imshow("Img window", cv_img)

    # write image to a file
    cv.imwrite('camera_img.jpg', cv_img)

    # hold script till terminate key is pressed
    key = cv.waitKey(0)
    if key == ord("s"):
        cv.destroyAllWindows()



if __name__=='__main__':
    main()