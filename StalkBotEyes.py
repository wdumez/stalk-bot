
import cv2
from cascade_filter import Cascade_filter
from full_body_detector import Full_body_detector

def drawRectangles(frame, rects, color):
    for idx, (column, row, width, height) in enumerate(rects):
        cv2.rectangle(
            frame,
            (column, row),
            (column + width, row + height),
            color,
            2
        )
    return frame


def determine_action(rects_faces, rects_full_body, rects_upper_body, rects_lower_body):
    action="Niks"
    if (len(rects_full_body) == 0 and len(rects_faces) == 0 and len(rects_upper_body) == 0):
        action="Zoeken"
    if ((len(rects_full_body) != 0 or len(rects_upper_body) != 0) and len(rects_faces) == 0):
        action="Rijden"
    if (len(rects_faces) != 0):
        action="Stoppen"

    return action

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
        frame=drawRectangles(frame, rects_full_body, (255,0,0))

        #Detect Faces
        rects_faces=face_detector.detect(gray)
        frame=drawRectangles(frame, rects_faces, (0,255,0))

        #Upper body
        rects_upper_body=upper_body_detector.detect(gray)
        frame=drawRectangles(frame, rects_upper_body, (0,0,255))

        #Lower body
        rects_lower_body=lower_body_detector.detect(gray)
        frame = drawRectangles(frame, rects_lower_body, (0, 255, 255))

        action=determine_action(rects_faces, rects_full_body, rects_upper_body, rects_lower_body)

        cv2.putText(frame, action, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color=(255, 255, 0))

        cv2.imshow('Frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()




if __name__ == "__main__":
    main()

