"""Contains the node for making the turtlebot move."""
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from stalkbot_interface.msg import PersonOpenCv,BoundingBox
from stalkbot_interface.msg import MoveCommand


class MovementController(Node):
    """Makes the turtlebot move according to incoming commands."""

    MOVEMENT_UPDATE_TIME = 0.01  # seconds
    MOVE_SPEED = 0.1
    ROTATE_SPEED = 0.25

    def __init__(self):
        super().__init__('movement_controller')
        self.vel_msg = Twist()
        self.vel_msg.linear.x = 0.0
        self.vel_msg.angular.z = 0.0
        # Parameters that do not change
        self.vel_msg.linear.y = 0.0
        self.vel_msg.linear.z = 0.0
        self.vel_msg.angular.x = 0.0
        self.vel_msg.angular.y = 0.0

        self.move_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

        # Move timer sends the Twist message to move the robot
        self.move_timer = self.create_timer(
            MovementController.MOVEMENT_UPDATE_TIME,
            self.pubish_msg  # callback
        )

        # Subscribe to the incoming commands
        self.subscription = self.create_subscription(
            MoveCommand,  # msg type
            'move_command',  # topic name
            self.update_move_commands,  # callback
            10)  # queue size?
        self.subscription  # prevent unused variable warning

    def update_move_commands(self, msg):
        """
        Update self.vel_msg with the right
        parameters according to the current state.
        """
        # ! You must specify these values as float,
        # ! otherwise you will get an error.
        # positive linear x is move forward
        # positive angular z is rotate right
        # self.get_logger().info('Updating commands based on incoming msg')
        if msg.move_forward:
            self.vel_msg.linear.x = MovementController.MOVE_SPEED
        else:
            self.vel_msg.linear.x = 0.0
        if msg.rotate_left:
            self.vel_msg.angular.z = MovementController.ROTATE_SPEED
        elif msg.rotate_right:
            self.vel_msg.angular.z = -MovementController.ROTATE_SPEED
        else:
            self.vel_msg.angular.z = 0.0

    def pubish_msg(self):
        """Publish the Twist message to make the robot move."""
        # self.get_logger().info('Publishing move commands to cmd_vel')
        self.move_publisher.publish(self.vel_msg)


def main(args=None):
    rclpy.init(args=args)

    movement_controller = MovementController()

    rclpy.spin(movement_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    movement_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
