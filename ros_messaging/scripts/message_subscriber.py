#!/usr/bin/env python

import rospy

from std_msgs.msg import String


class MessageSubscriber:

    def __init__(
            self,
            node_name,
            topic_name
    ):
        rospy.init_node(node_name)

        self._topic_name = topic_name
        self._subscriber = rospy.Subscriber(
            self._topic_name,
            String,
            callback=self._callback,
            queue_size=1)

    def _callback(self, msg):
        rospy.loginfo("I heard: {}".format(msg.data))


if __name__ == "__main__":
    message_subscriber = MessageSubscriber("message_subscriber", "example_messaging/messages")
    rospy.spin()
