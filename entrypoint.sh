#!/bin/sh

roscd; cd ..
catkin_make
source devel/setup.bash
rostest ros_messaging test_message_publisher.test