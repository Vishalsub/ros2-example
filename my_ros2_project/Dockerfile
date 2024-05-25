FROM osrf/ros:humble-desktop-full

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# Copy the package
COPY . /my_ros2_project
WORKDIR /my_ros2_project

# Make entrypoint script executable
#RUN chmod +x /my_ros2_project/docker/entrypoint.sh

# Build the package
RUN . /opt/ros/humble/setup.sh && colcon build

# Source the environment and run the node
#ENTRYPOINT ["/my_ros2_project/docker/entrypoint.sh"]
