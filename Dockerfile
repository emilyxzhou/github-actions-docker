FROM ros:kinetic-ros-base-xenial

RUN \
	mkdir -p /root/catkin_ws/src \
	&& cd /root/catkin_ws/src

COPY . /root/catkin_ws/src

RUN chmod +x /root/catkin_ws/src/entrypoint.sh \
    && /bin/bash -c "source /opt/ros/kinetic/setup.bash" \
    && roscd; cd .. \
    && catkin_make

ENTRYPOINT ["/root/catkin_ws/src/entrypoint.sh"]