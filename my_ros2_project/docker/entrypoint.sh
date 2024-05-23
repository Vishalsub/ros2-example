#!/bin/bash
set -e

# Source ROS 2 setup
source /opt/ros/humble/setup.bash
source /my_ros2_project/install/setup.bash

# Execute the command
exec "$@"
