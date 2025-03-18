import rclpy
from rclpy.node import Node

import time

from std_msgs.msg import Float64MultiArray

class VelocityPub(Node):
    def __init__(self):
        super().__init__('velocity_publisher')
        self.get_logger().info("Velocity publisher initialized...")
        self.publisher_ = self.create_publisher(Float64MultiArray, 'forward_velocity_controller/commands', 10)
    
        # state variables
        self.velocity = [1.0, 1.0, 1.0, 1.0]
    
        self.loop()
    
    
    
    ### Publishes constant velocity at 1 Hz (10 times) ### 
    def loop(self):
        while True
            msg = Float64MultiArray()
            msg.data = self.velocity
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.publisher_.publish(msg)
            time.sleep(1)


def main(args=None):
    rclpy.init(args=args)

    velocity_publisher = VelocityPub()

    rclpy.spin(velocity_publisher)

    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
