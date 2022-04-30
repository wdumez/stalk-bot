from ast import Try
import cv2
from numpy import rec
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from stalkbot_interface.msg import BoundingBox, PersonOpenCv
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

class CameraController(Node):

    def __init__(self):
        super().__init__('camera_controller')

        self.publisher_ = self.create_publisher(PersonOpenCv, 'persons', 10)
        self.processedImage = self.create_publisher(Image, 'video_frames', 10)
        self.br = CvBridge()

        #making detectors
        self.full_body_detector=Full_body_detector()
        self.face_detector=Cascade_filter(0)
        self.upper_body_detector = Cascade_filter(1)
        self.lower_body_detector = Cascade_filter(2)
        

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.get_logger().info('Cap is not opened')
            self.cap.open()
        if not self.cap.isOpened():
            self.get_logger().info('Cap did still not open')
        FPS = 10
        PUBLISH_TIME = 1 / FPS
        self.timer = self.create_timer(PUBLISH_TIME, self.verwerkFoto)

    def verwerkFoto(self):
        ret, frame = self.cap.read()
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

        #prepare output
        self.get_logger().info('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        self.msg = PersonOpenCv()
        self.msg.w = frame.shape[0]

        Null = BoundingBox()
        Null.x = -1
        Null.y = -1
        Null.xx = -1
        Null.yy = -1

        try:
            self.get_logger().info('Faces: "%s"' % rects_faces)
            rects = BoundingBox()
            rects.x = int(rects_faces[0][0])
            rects.y = int(rects_faces[0][1])
            rects.xx = int(rects_faces[0][2])
            rects.yy = int(rects_faces[0][3])
            self.msg.persons.append(rects)

            frame = cv2.rectangle(frame, (rects.x, rects.y, rects.xx, rects.yy), (250, 0, 0), 2)
        except:
            self.get_logger().info('No Face')
            self.msg.persons.append(Null)
        try:
            self.get_logger().info('Body: "%s"' % rects_full_body)
            rects = BoundingBox()
            rects.x = int(rects_full_body[0][0])
            rects.y = int(rects_full_body[0][1])
            rects.xx = int(rects_full_body[0][2])
            rects.yy = int(rects_full_body[0][3])
            self.msg.persons.append(rects)

            frame = cv2.rectangle(frame, (rects.x, rects.y, rects.xx, rects.yy), (0, 0, 255), 2)

        except:
            self.get_logger().info('No full body')
            self.msg.persons.append(Null)

        try:
            self.get_logger().info('Upper: "%s"' % rects_upper_body)
            rects = BoundingBox()
            rects.x = int(rects_upper_body[0][0])
            rects.y = int(rects_upper_body[0][1])
            rects.xx = int(rects_upper_body[0][2])
            rects.yy = int(rects_upper_body[0][3])
            self.msg.persons.append(rects)

            frame = cv2.rectangle(frame, (rects.x, rects.y, rects.xx, rects.yy), (0, 255, 0), 2)

        except:
            self.get_logger().info('No upper body')
            self.msg.persons.append(Null)

        try:
            self.get_logger().info('Lower: "%s"' % rects_lower_body)
            rects = BoundingBox()
            rects.x = int(rects_lower_body[0][0])
            rects.y = int(rects_lower_body[0][1])
            rects.xx = int(rects_lower_body[0][2])
            rects.yy = int(rects_lower_body[0][3])
            self.msg.persons.append(rects)

            frame = cv2.rectangle(frame, (rects.x, rects.y, rects.xx, rects.yy), (250, 255, 0), 2)

        except:
            self.get_logger().info('No lower body')
            self.msg.persons.append(Null)


        #send output
        self.publisher_.publish(self.msg)
        self.processedImage.publish(self.br.cv2_to_imgmsg(frame, encoding="bgr8"))     


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = CameraController()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
