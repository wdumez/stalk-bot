import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MovementController(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.vel_msg = Twist()
        
        # Current state
        self.move_forward = False
        self.rotate_right = False
        self.rotate_left = False
        
        self.move_publisher = self.create_publisher('cmd_vel', Twist, queue_size=10)
        
        # Move timer sends the Twist message to move the robot
        move_timer_period = 0.01  # seconds
        self.move_timer = self.create_timer(move_timer_period, self.send_move_commands)
        
        # Sample timer samples the current commmands
        # TODO replace with our custom message
        # self.subscription = self.create_subscription(
        #     Twist,
        #     'topic',
        #     self.listener_callback,
        #     10)
        # self.subscription  # prevent unused variable warning
        
        # TODO currently fake some commands
        get_commands_period = 0.1 # seconds
        self.get_commands_timer = self.create_timer(get_commands_period, self.get_commands)
        
    def get_commands(self):
        if self.move_forward:
            self.move_forward = False
        if self.rotate_left:
            self.rotate_left = False
            self.rotate_right = True
        else:
            self.rotate_left = True
            self.rotate_right = False
        

    def send_move_commands(self):
        # TODO linear and angular velocity calculation based on current state
        # positive x is forward
        if self.move_forward:
            self.vel_msg.linear.x = 10
        else:
            self.vel_msg.linear.x = 0
        # positive y is left
        self.vel_msg.linear.y = 0
        # positive z is up
        self.vel_msg.linear.z = 0
        
        # ? positive x is ?
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0
        self.move_publisher.publish(self.vel_msg)
        self.get_logger().info('Sent move commands: ' + self.vel_msg)


def main(args=None):
    rclpy.init(args=args)

    movementController = MovementController()

    rclpy.spin(movementController)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    movementController.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()