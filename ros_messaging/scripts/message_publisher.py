#!/usr/bin/env python

import rospy

from std_msgs.msg import String


class MessagePublisher:

    def __init__(
            self,
            node_name,
            topic_name
    ):
        rospy.init_node(node_name)

        self._topic_name = topic_name
        self._publisher = rospy.Publisher(self._topic_name, String, queue_size=1)

    def publish(self, message):
        rospy.loginfo("Publishing: {}".format(message))
        self._publisher.publish(message)


if __name__ == "__main__":
    message_publisher = MessagePublisher("message_publisher", "example_messaging/messages")
    rospy.sleep(2)
    while not rospy.is_shutdown():
        message_publisher.publish("Hello there!")
        rospy.sleep(2)
