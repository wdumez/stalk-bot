
from tkinter import W

from matplotlib.style import available
import rclpy
from rclpy.node import Node
from stalkbot_interface.msg import MoveCommand, PersonOpenCv



class MainController(Node):
    """"Makes the movement decision, based on detected persons"""

    def __init__(self):
        super().__init__('main_controller')

        self.main_msg = MoveCommand()

        self.main_publisher = self.create_publisher(MoveCommand, 'move_command', 10)
        
        # Subscribe to the incoming commands
        self.subscription = self.create_subscription(
            PersonOpenCv,  # msg type
            'main_command',  # topic name !!!!!!!!!!
            self.send_main_commands,  # callback
            10)  # queue size?
        self.subscription  # prevent unused variable warning


    def unpack(rects):
        middle = 0
        rects_not_empty = 0
        try:
            for column, row, width, height in rects:
                print(column, width)
                middle = column + (width/2)
                rects_not_empty = 1
        except:
            print("Ween")
            
        return middle, rects_not_empty



    def send_main_command(self, msg): 
        
        middle_screen = image_width/2
        window = (middle_screen - 20, middle_screen + 21)

        #unpack the rects received: rects_full_body_not_empty=1 of not empty
        middle_full_body, rects_full_body_not_empty = unpack(rects_full_body)
        middle_upper_body, rects_upper_body_not_empty = unpack(rects_upper_body)
        middle_lower_body, rects_lower_body_not_empty = unpack(rects_lower_body)

        #voor debuggen
        #rects_faces = []
        
        #try to calculate avarage middle, if there are no body rects will fail
        try:
            average_middle = (middle_full_body + middle_upper_body + middle_lower_body)/(rects_full_body_not_empty + rects_upper_body_not_empty + rects_lower_body_not_empty)
            print(f"avarge middle: {average_middle}") 
        except:
            print("alles leeg")

        #if one faces is detected send message "Stoppen"
        if(len(rects_faces) != 0):
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
                self.main_msg.rotate_left = True
                self.main_msg.rotate_right = False
                self.main_publisher.publish(self.main_msg)
                return
            #person is on the left of the screen
            if(average_middle < window[0]):
                self.main_msg.move_forward = False
                self.main_msg.rotate_left = False
                self.main_msg.rotate_right = True
                self.main_publisher.publish(self.main_msg)
                return
            #if none of these are fullfilled --> person is in the window you can drive forward
            self.main_msg.move_forward = True
            self.main_msg.rotate_left = False
            self.main_msg.rotate_right = False
            self.main_publisher.publish(self.main_msg)
            return
            
        #nothing detected at all --> search a person
        self.main_msg.move_forward = False
        self.main_msg.rotate_left = False
        self.main_msg.rotate_right = True
        self.main_publisher.publish(self.main_msg)
        return

       




