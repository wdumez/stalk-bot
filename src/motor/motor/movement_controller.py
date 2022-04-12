"""Contains the node for making the turtlebot move."""
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
# from stalkbot_interface.msg import Person


class MovementController(Node):
    """Makes the turtlebot move according to incoming commands."""

    MOVEMENT_UPDATE_TIME = 1  # seconds
    MOVE_SPEED = 0.2

    def __init__(self):
        super().__init__('minimal_publisher')
        self.vel_msg = Twist()
        # Parameters that do not change

        # Current state
        self.move_forward = False
        self.rotate_right = False
        self.rotate_left = False

        self.move_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

        # Move timer sends the Twist message to move the robot
        self.move_timer = self.create_timer(
            MovementController.MOVEMENT_UPDATE_TIME,
            self.send_move_commands  # callback
        )

        # Subscribe to the incoming commands
        # TODO no custom message yet
        # self.subscription = self.create_subscription(
        #     MoveCommands, # msg type
        #     'topic_name', # topic name
        #     self.send_move_commands, # callback
        #     10) # queue size?
        # self.subscription  # prevent unused variable warning

        # TODO currently faking some commands
        get_commands_period = 5  # seconds
        self.get_commands_timer = self.create_timer(
            get_commands_period, self.get_commands)

    def get_commands(self):
        """Dummy function to simulate some commands (alternates)."""
        if self.move_forward:
            self.move_forward = False
        else:
            self.move_forward = True
        if self.rotate_left:
            self.rotate_left = False
            self.rotate_right = True
        else:
            self.rotate_left = True
            self.rotate_right = False
        self.get_logger().info("Updated state with new commands\n.")

    def send_move_commands(self):
        """
        Update and publish self.vel_msg with the right
        parameters according to the current state.
        """
        # TODO linear and angular velocity calculation based on current state
        # ! You must specify these values as float,
        # ! otherwise you will get an error.
        # positive x is forward
        if self.move_forward:
            self.vel_msg.linear.x = 0.2
        else:
            self.vel_msg.linear.x = 0.0
        if self.rotate_left:
            self.vel_msg.angular.z = 0.2
        elif self.rotate_left:
            self.vel_msg.angular.z = -0.2
        else:
            self.vel_msg.angular.z = 0.0
        self.move_publisher.publish(self.vel_msg)
        self.get_logger().info('Sent move commands: \n%s\n' % str(self.vel_msg))


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
