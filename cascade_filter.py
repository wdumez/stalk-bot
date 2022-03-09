import cv2

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