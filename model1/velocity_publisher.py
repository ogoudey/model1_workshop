import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor

import time

from std_msgs.msg import Float64MultiArray

# imports from pip
from gpiozero import Motor

class VelocityPub(Node):
    def __init__(self):
        super().__init__('velocity_publisher')
        
        # TODO: Move these parameters to main()?
        reality_level_descriptor = ParameterDescriptor(description='Put "actual" or "sim".')
        self.declare_parameter('reality', 'sim', reality_level_descriptor)
        reality_level = self.get_parameter('reality').get_parameter_value().string_value

        self.get_logger().info("Velocity publisher initialized... with reality level: " + reality_level)
                
        teleop_param_descriptor = ParameterDescriptor(description='Put "teleop" or "auto".')
        self.declare_parameter('teleop', 'auto', teleop_param_descriptor)
        teleop_param = self.get_parameter('teleop').get_parameter_value().string_value
        
        self.get_logger().info("Input is " + teleop_param)
          
        # common state variables
        self.velocity = [1.0, 1.0, 1.0, 1.0]
        
        # Set input to teleop/auto
        
        if reality_level == "sim":
            self.publisher_ = self.create_publisher(Float64MultiArray, 'forward_velocity_controller/commands', 10)    
        
            # main loop
            self.loop()
        elif reality_level == "actual":
            # Options:
            # 1. Create new publisher and have the main loop run in common (pass teleoperator as arg?)
            # 2. Create new loop w or w/o publisher
            #
            #
            #
            #
            pass
            
    
    
    
    ### Publishes constant velocity at 1 Hz ### 
    def loop(self):
        while True:
            msg = Float64MultiArray()
            msg.data = self.velocity
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.publisher_.publish(msg)
            time.sleep(1)


def main(args=None):
    rclpy.init(args=args) # ??

    
    velocity_publisher = VelocityPub()

    rclpy.spin(velocity_publisher)

    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
