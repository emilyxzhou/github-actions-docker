FROM ros:kinetic-ros-base-xenial

RUN \
	mkdir -p /root/catkin_ws/src \
	&& cd /root/catkin_ws/src

COPY . /root/catkin_ws/src

RUN \
	cd /root/catkin_ws \
	&& /bin/bash -c "source /opt/ros/kinetic/setup.bash && catkin_make"

RUN chmod +x /root/catkin_ws/src/entrypoint.sh

ENTRYPOINT ["bash" "/root/catkin_ws/src/entrypoint.sh"]