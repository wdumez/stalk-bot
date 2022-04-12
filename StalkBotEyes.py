
import cv2
from cascade_filter import Cascade_filter
from full_body_detector import Full_body_detector
from MainController import MainController



def main():
    capture = cv2.VideoCapture(0)

    #initialize the detectors
    full_body_detector=Full_body_detector()
    face_detector=Cascade_filter(0)
    upper_body_detector = Cascade_filter(1)
    lower_body_detector = Cascade_filter(2)

    while True:
        #this would be a frame that would be received from camera node
        ret, frame = capture.read()
        #do the needed pre-proccesing
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
        
        #Publish all the rects above here
       

       #Actie voor test, mag verwijdert worden in node
        action = MainController(gray.shape[1], rects_faces, rects_full_body, rects_upper_body, rects_lower_body)

        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (30, 30)
        fontScale = 0.8
        color = (0, 0, 0)
        thickness = 1

        print(rects_faces, rects_full_body, rects_upper_body, rects_lower_body) 
        try:
            frame = cv2.rectangle(frame, (rects_faces[0][0], rects_faces[0][1]), (rects_faces[0][0] + rects_faces[0][2], rects_faces[0][1] + rects_faces[0][3]), (255, 0, 0), 2) 
        except:
            print("Leeg")
        try:
            frame = cv2.rectangle(frame, (rects_full_body[0][0], rects_full_body[0][1]), (rects_full_body[0][0] + rects_full_body[0][2], rects_full_body[0][1] + rects_full_body[0][3]), (0, 255, 0), 2) 
        except:
            print("Leeg")
        try:
            frame = cv2.rectangle(frame, (rects_upper_body[0][0], rects_upper_body[0][1]), (rects_upper_body[0][0] + rects_upper_body[0][2], rects_upper_body[0][1] + rects_upper_body[0][3]), (0, 0, 255), 2) 
        except:
            print("Leeg")
        try:
            frame = cv2.rectangle(frame, (rects_lower_body[0][0], rects_lower_body[0][1]), (rects_lower_body[0][0] + rects_lower_body[0][2], rects_lower_body[0][1] + rects_lower_body[0][3]), (255, 255, 0), 2) 
        except:
            print("Leeg")
        frame = cv2.putText(frame, action, org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)

        cv2.imshow("Detection with Action", frame) 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

