#!/usr/bin env python2

import rospy
from std_msgs.msg import Int32MultiArray

def callback_1(data):
    global pub1
    pub1 = rospy.Publisher("uc_vels", type, queue_size=10)
    pub1.publish(data.data)

def callback_2(data):   
    global pub2
    pub2 = rospy.Publisher("uc_angs", type, queue_size=10)
    pub2.publish(data.data)

def main():
    rospy.init_node('rover_control', anonymous=True)
    rospy.Subscriber('wheel_vels', Int32MultiArray, callback_1)
    rospy.Subscriber('wheel_angs', Int32MultiArray, callback_2)
    rospy.spin()

if __name__ == '__main__':
    main()