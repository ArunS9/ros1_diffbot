#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def laser_callback(msg):
    # Filter the laser scan data to have only a range of 0 to 120 degrees
    filtered_ranges = msg.ranges[:120]  # Consider ranges from 0 to 120 degrees
    
    # Create a new LaserScan message to publish filtered data
    filtered_msg = LaserScan()
    filtered_msg.header = msg.header
    filtered_msg.angle_min = msg.angle_min
    filtered_msg.angle_max = msg.angle_max
    filtered_msg.angle_increment = msg.angle_increment
    filtered_msg.time_increment = msg.time_increment
    filtered_msg.scan_time = msg.scan_time
    filtered_msg.range_min = msg.range_min
    filtered_msg.range_max = msg.range_max
    filtered_msg.ranges = filtered_ranges
    
    # Publish the filtered laser scan data to the '/filtered_scan' topic
    pub.publish(filtered_msg)

def main():
    rospy.init_node('laser_reader')  # Initialize the ROS node with name 'laser_reader'
    
    # Subscribe to the '/scan' topic to receive laser scan data
    rospy.Subscriber('/scan', LaserScan, laser_callback)
    
    # Create a publisher for the filtered laser scan data
    global pub
    pub = rospy.Publisher('/filtered_scan', LaserScan, queue_size=10)
    
    # Spin keeps the node running and listens for incoming messages
    rospy.spin()

if __name__ == '__main__':
    main()

