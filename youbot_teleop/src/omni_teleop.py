#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class omni_teleop(object):
    def __init__(self):
        rospy.init_node('youbot_teleop')
        self.twist_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.twist = Twist()
        self.joy_to_vel()

    def joystick_callback(self, data):
        scale = 1
        self.twist.linear.x  = scale*data.axes[1]
        self.twist.linear.y  = scale*data.axes[0]
        self.twist.angular.z = scale*data.axes[2]

    # Intializes everything
    def joy_to_vel(self):
        rate = rospy.Rate(10) # 10 Hz loop rate
        while not rospy.is_shutdown():
            # Subscriber(s)
            rospy.Subscriber("joy", Joy, self.joystick_callback)
            # Publisher(s)
            self.twist_publisher.publish(self.twist)
            # Sleep until the next loop
            rate.sleep()

if __name__ == '__main__':
    omni_teleop()
