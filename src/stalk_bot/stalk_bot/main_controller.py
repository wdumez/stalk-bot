import rclpy
from rclpy.node import Node
from stalkbot_interface.msg import MoveCommand, PersonOpenCv, BoundingBox



class MainController(Node):
    """"Makes the movement decision, based on detected persons"""

    def __init__(self):
        super().__init__('main_controller')

        self.main_msg = MoveCommand()

        self.main_publisher = self.create_publisher(MoveCommand, 'move_command', 10)
        
        # Subscribe to the incoming commands
        self.subscription = self.create_subscription(
            PersonOpenCv,  # msg type
            'persons',  # topic name
            self.send_main_command,  # callback
            10)  # queue size?
        self.subscription  # prevent unused variable warning
        

    # Function that unpacks rectangle lists and returns if it was empty or where middle is
    def unpack(self, Box):
        middle = 0
        rects_not_empty = 0
        try:
            if(Box.x < 0):
                raise ValueError
            print(Box.x, Box.xx)
            middle = Box.x + (Box.xx/2)
            rects_not_empty = 1
        except Exception as e:
            print(e)
    
            
        return middle, rects_not_empty

    #Defines how large the window has to be
    WINDOW_WIDTH = 40

    def send_main_command(self, msg): 
        
        middle_screen = msg.w/2
        window = (middle_screen - MainController.WINDOW_WIDTH, middle_screen + MainController.WINDOW_WIDTH)

        #unpack the rects received: rects_full_body_not_empty=1 of not empty
        middle_full_body, rects_full_body_not_empty = self.unpack(msg.persons[1])
        middle_upper_body, rects_upper_body_not_empty = self.unpack(msg.persons[2])
        middle_lower_body, rects_lower_body_not_empty = self.unpack(msg.persons[3])

        rects_faces = msg.persons[0]
        #voor debuggen
        #rects_faces = []
        
        #try to calculate avarage middle, if there are no body rects will fail
        try:
            average_middle = (middle_full_body + middle_upper_body + middle_lower_body)/(rects_full_body_not_empty + rects_upper_body_not_empty + rects_lower_body_not_empty)
            print(f"avarge middle: {average_middle}") 
        except:
            print("alles leeg")

        #if one faces is detected send message "Stoppen"
        if(rects_faces.x > 0 ):
            self.main_msg.move_forward = False
            self.main_msg.rotate_left = False
            self.main_msg.rotate_right = False
            self.main_publisher.publish(self.main_msg)
            return

        #when there is atleast one body and no faces detected
        if((rects_full_body_not_empty or rects_upper_body_not_empty or rects_lower_body_not_empty)):
            #person is on the right of the screen
            if(average_middle > window[1]):
                self.main_msg.move_forward = False
                self.main_msg.rotate_left = False
                self.main_msg.rotate_right = True
                self.main_publisher.publish(self.main_msg)
                return
            #person is on the left of the screen
            if(average_middle < window[0]):
                self.main_msg.move_forward = False
                self.main_msg.rotate_left = True
                self.main_msg.rotate_right = False
                self.main_publisher.publish(self.main_msg)
                return
            #if none of these are fullfilled --> person is in the window you can drive forward
            self.main_msg.move_forward = True
            self.main_msg.rotate_left = False
            self.main_msg.rotate_right = False
            self.main_publisher.publish(self.main_msg)
            return
            
        self.main_msg.move_forward = False
        self.main_msg.rotate_left = False
        self.main_msg.rotate_right = True
        self.main_publisher.publish(self.main_msg)
        return

       

def main(args=None):
    rclpy.init(args=args)

    main_controller = MainController()

    rclpy.spin(main_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    main_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()



