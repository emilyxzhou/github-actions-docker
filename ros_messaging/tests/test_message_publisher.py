#!/usr/bin/env python

import rospy
import rostest
import unittest

from std_msgs.msg import String

PKG = "ros_messaging"
NAME = "test_message_publisher"
_PUBLISHER_NODE = "message_publisher"

_MESSAGE_TOPIC = "example_messaging/messages"


class TestMessagePublisher(unittest.TestCase):

    def test_message_publisher(self):
        assert rostest.is_publisher(
            rospy.resolve_name(_MESSAGE_TOPIC),
            rospy.resolve_name(_PUBLISHER_NODE)
        )


if __name__ == "__main__":
    rospy.init_node(NAME)
    rostest.rosrun(PKG, NAME, TestMessagePublisher)
