import cv2

#This class uses a HOG descripter to detect full body persons in a gray scale image
class Full_body_detector():

    def __init__(self, ):
        self.full_body_detect = cv2.HOGDescriptor()
        self.full_body_detect.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect_full_body(self, gray_frame):
        detected_persons = self.full_body_detect.detectMultiScale(gray_frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
        rects, weights = detected_persons
        return rects