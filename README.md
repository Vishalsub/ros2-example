# My ROS2 Project

This is a simple ROS2 project to demonstrate package organization, Docker integration, CI/CD with GitHub Actions, and testing.

![GitHub top language](https://img.shields.io/github/languages/top/{Vishalsub}/{ros2-example}?color=yellow)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/{Vishalsub}/{ros2-example})
![GitHub forks](https://img.shields.io/github/forks/{Vishalsub}/{ros2-example}?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/{Vishalsub}/{ros2-example}?style=social)

## Installation
```bash
# Clone the repository
git clone https://github.com/Vishalsub/ros2-example .git
# change dir
cd your_repository
   ```

## How to Build and Run

### Using Docker

Build the Docker image:

```bash

cd my_ros2_projects/docker  

docker build -t my_ros2_project .

```

### Without Docker

Source ROS2 environment and build:

```bash
# source ros env
source /opt/ros/humble/setup.bash

# buid ros workspace
colcon build

# source ros workspace
source install/setup.bash

# Run your first node
ros2 run my_package my_node
```



## Contributing
Thank you for considering contributing to this project! Please check out the Contributing Guidelines.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Code of Conduct
Please adhere to our Code of Conduct to foster an open and welcoming environment.

## Security Policy
If you discover any security-related issues, please contact us at []. All security vulnerabilities will be promptly addressed.

## Issues
To report a bug or request a feature, please open an Issue.

## Pull Requests
We welcome Pull Requests! Please follow our Pull Request Template when submitting one.