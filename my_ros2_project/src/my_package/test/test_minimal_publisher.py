import os
import unittest

import launch
import launch_ros.actions
import launch_testing
import pytest
from launch_ros.actions import Node
from rclpy.node import Node as RclpyNode
from std_msgs.msg import String
import rclpy

class TestMinimalPublisher(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        rclpy.init()

    @classmethod
    def tearDownClass(cls):
        rclpy.shutdown()

    def setUp(self):
        self.node = RclpyNode('test_node')
        self.subscription = self.node.create_subscription(
            String,
            'topic',
            self.callback,
            10
        )
        self.received_messages = []

    def tearDown(self):
        self.node.destroy_node()

    def callback(self, msg):
        self.received_messages.append(msg.data)

    def test_publisher(self):
        # Launch the MinimalPublisher node
        node_action = Node(
            package='my_package',
            executable='my_pub_node',
            name='my_pub_node'
        )

        # Create and run the launch service
        launch_service = launch.LaunchService()
        launch_service.include_launch_description(launch.LaunchDescription([node_action]))
        launch_service.run()

        # Wait for some messages to be received
        rclpy.spin_once(self.node, timeout_sec=5)
        
        self.assertGreater(len(self.received_messages), 0)
        for i, message in enumerate(self.received_messages):
            self.assertEqual(message, f'Hello World: {i}')

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun('my_package', 'test_minimal_publisher', TestMinimalPublisher)
