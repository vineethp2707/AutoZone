#!/usr/bin/env python3

import rospy
import serial
from std_msgs.msg import String

def esp_to_ros():

    # Initialize the node
    rospy.init_node('esp_to_ros')

    # Get the USB port and baud rate from ROS parameter server
    port = rospy.get_param('~port', '/dev/ttyUSB0')
    baudrate = rospy.get_param('~baudrate', 115200)

    # Set up the serial connection
    ser = serial.Serial(port, baudrate, timeout=1)

    # Set up the ROS publisher
    pub = rospy.Publisher('esp_data', String, queue_size=10)

    # Set the loop rate in Hz
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        # Read the serial data
        data = ser.readline().strip().decode('ascii')
        print(data)

        # Publish the data onto the ROS topic
        pub.publish(data)

        # Sleep for the remainder of the loop cycle
        rate.sleep()

if __name__ == '__main__':
    try:
        esp_to_ros()
    except rospy.ROSInterruptException:
        pass

