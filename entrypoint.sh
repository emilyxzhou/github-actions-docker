#!/bin/sh

cd /root/catkin_ws
/bin/bash -c "source /opt/ros/kinetic/setup.bash " && catkin_make
rostest ros_messaging test_message_publisher.test