#!/usr/bin/env python3

import rospy
from serial import Serial
from std_msgs.msg import String

# Set up ROS node and publisher
rospy.init_node('usb_publisher')
pub = rospy.Publisher('usb_data', String, queue_size=10)

# Set up serial connection to USB device
ser = Serial('/dev/ttyUSB0', 9600)

# Continuously read data from USB device and publish on ROS topic
while not rospy.is_shutdown():
    data = ser.readline().strip()
    pub.publish(data)
