# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ast import Try
import rclpy
from rclpy.node import Node
import cv2

from std_msgs.msg import String

class Cascade_filter():
    def __init__(self, number):
        try:
            if(number<0 or number>2):
                raise Exception("Value has to be between 0 and 2")
            if(number == 0):
                self.detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
            if (number == 1):
                self.detector= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_upperbody.xml")
            if (number == 2):
                self.detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_lowerbody.xml")
        except Exception as er:
            print("Value has to be between 0 and 2")

    def detect(self, gray_frame):
        detected_upper = self.detector.detectMultiScale3(gray_frame, outputRejectLevels=True)
        rects, weights, score = detected_upper

        return rects

class Full_body_detector():

    def __init__(self, ):
        self.full_body_detect = cv2.HOGDescriptor()
        self.full_body_detect.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect_full_body(self, gray_frame):
        detected_persons = self.full_body_detect.detectMultiScale(gray_frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
        rects, weights = detected_persons
        return rects

class MinimalSubscriber(Node):
    
    FPS = 30
    PUBLISH_TIME = 1 / FPS

    def __init__(self):
        super().__init__('minimal_subscriber')
        """self.subscription = self.create_subscription(
            String,
            'camera_topic',
            self.listener_callback,
            10)"""
        self.publisher_ = self.create_publisher(String, 'rects_topic', 10)

        #self.subscription  # prevent unused variable warning
        self.full_body_detector=Full_body_detector() #making detectors
        self.face_detector=Cascade_filter(0)
        self.upper_body_detector = Cascade_filter(1)
        self.lower_body_detector = Cascade_filter(2)
        
        self.publish_timer = self.create_timer(
            MinimalSubscriber.PUBLISH_TIME,
            self.publish_msg
        )
        
    def publish_msg(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        #cv2.imshow('frame', frame)
        self.verwerkFoto(frame)


    def verwerkFoto(self, frame):

        frame=cv2.resize(frame, (320, 240), interpolation = cv2.INTER_AREA)
        gray=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        #Detect Persons
        rects_full_body=self.full_body_detector.detect_full_body(gray)
        #Detect Faces
        rects_faces=self.face_detector.detect(gray)
        #Upper body
        rects_upper_body=self.upper_body_detector.detect(gray)
        #Lower body
        rects_lower_body=self.lower_body_detector.detect(gray)

        #print output
        self.get_logger().info('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        try:
            self.get_logger().info('Faces: "%s"' % rects_faces)
        except:
            self.get_logger().info('No Face')
        try:
            self.get_logger().info('Body: "%s"' % rects_full_body)
        except:
            self.get_logger().info('No full body')
        try:
            self.get_logger().info('Upper: "%s"' % rects_upper_body)
        except:
            self.get_logger().info('No upper body')
        try:
            self.get_logger().info('Lower: "%s"' % rects_lower_body)
        except:
            self.get_logger().info('No lower body')

        #Hier moet je message publishen
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
