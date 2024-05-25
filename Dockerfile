FROM osrf/ros:humble-desktop-full

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    x11-apps \
    xauth \
    libxcb-xinerama0 \
    libxcb-xinput0 \
    libxkbcommon-x11-0 \
    qt5-qmake \
    qtbase5-dev \
    qtbase5-dev-tools \
    && rm -rf /var/lib/apt/lists/*

# Copy the package
COPY . /my_ros2_project
WORKDIR /my_ros2_project

# Build the package
RUN . /opt/ros/humble/setup.sh && colcon build

# Source the environment and run the node
# ENTRYPOINT ["/my_ros2_project/docker/entrypoint.sh"]
