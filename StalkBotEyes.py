#!/usr/bin/env python
# coding: utf-8

# In[2]:

import cv2
import os
import numpy as np


# In[ ]:


ls


# #  Face detection

# In[ ]:


face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")


# In[ ]:


capture=cv2.VideoCapture(0)


# In[ ]:


while True:
    ret, frame = capture.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    detected_faces = face_cascade.detectMultiScale3(gray, outputRejectLevels=True)
    rects,weights, score=detected_faces
    for idx, (column, row, width, height) in enumerate(rects):
    
        cv2.rectangle(
            frame,
            (column, row),
            (column + width, row + height),
            (0, 255, 0),
            2
        )
    
    cv2.imshow('Frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()


# # Full Body detection

# In[ ]:


capture=cv2.VideoCapture(0)


# In[ ]:


hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


# In[ ]:


while True:
    ret, frame = capture.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    detected_persons = hog.detectMultiScale(gray, winStride=(4,4), padding=(8,8), scale=1.05)
    rects,weights=detected_persons
    for idx, (column, row, width, height) in enumerate(rects):
    
        cv2.rectangle(
            frame,
            (column, row),
            (column + width, row + height),
            (0, 255, 0),
            2
        )
    
    cv2.imshow('Frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()


# # Combination

# ## 1. Initialize Webcam

# In[3]:


capture=cv2.VideoCapture(0)


# ## 2. Initialize detectors

# In[4]:


hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
person_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_upperbody.xml")


# ## 3. Loop

# In[5]:


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


# In[6]:


while True:
    ret, frame = capture.read()
    frame=cv2.resize(frame, (320, 240), interpolation = cv2.INTER_AREA)
    gray=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
    #Detect Persons
    detected_persons = hog.detectMultiScale(gray, winStride=(4,4), padding=(8,8), scale=1.05)
    rects,weights=detected_persons
    frame=drawRectangles(frame, rects, (255,0,0))
    
    #Detect Faces
    detected_faces = face_cascade.detectMultiScale3(gray, outputRejectLevels=True)
    rects,weights, score=detected_faces
    frame=drawRectangles(frame, rects, (0,255,0))
    
    #Detect Faces
    detected_upper = person_cascade.detectMultiScale3(gray, outputRejectLevels=True)
    rects,weights, score=detected_upper
    frame=drawRectangles(frame, rects, (0,0,255))
    
    
    if(len(detected_persons[0])==0 and len(detected_faces[0])==0 and len(detected_upper[0])==0):
        cv2.putText(frame, 'Zoeken', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color=(255, 255,0))
    
    if((len(detected_persons[0])!=0 or len(detected_upper[0])!=0) and len(detected_faces[0])==0):
        cv2.putText(frame, 'Rijden', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color=(255, 255,0))
    if(len(detected_faces[0])!=0):
        cv2.putText(frame, 'Stoppen', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color=(255, 255,0))
        
    
    cv2.imshow('Frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()


# In[ ]:




