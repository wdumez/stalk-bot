
import cv2
from cascade_filter import Cascade_filter
from full_body_detector import Full_body_detector




def main():
    capture = cv2.VideoCapture(0)

    full_body_detector=Full_body_detector()
    face_detector=Cascade_filter(0)
    upper_body_detector = Cascade_filter(1)
    lower_body_detector = Cascade_filter(2)

    while True:
        ret, frame = capture.read()
        frame=cv2.resize(frame, (320, 240), interpolation = cv2.INTER_AREA)
        gray=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        #Detect Persons
        rects_full_body=full_body_detector.detect_full_body(gray)
        #Detect Faces
        rects_faces=face_detector.detect(gray)
        #Upper body
        rects_upper_body=upper_body_detector.detect(gray)
        #Lower body
        rects_lower_body=lower_body_detector.detect(gray)
        
        #Hier moet je message publishen
    




if __name__ == "__main__":
    main()

