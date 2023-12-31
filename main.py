import cv2
import os
import pickle
import face_recognition
import numpy as np
import cvzone
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgBackground=cv2.imread('Resources/background.png')

#importing the mode images into a list
folderModePath='Resources/Modes'
modePathList=os.listdir(folderModePath)
imgModeList=[]
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
    
#Load the encoding file
file=open('EncodeFile.p','rb')
encodeListKnownWithIds=pickle.load(file)
file.close()
encodeListKnown,studentIds=encodeListKnownWithIds
#print(studentIds)
print("Encode file loaded")
while True:
    success,img=cap.read()
    imgS = cv2.resize(img, None, fx=0.25, fy=0.25)
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faceCurFrame=face_recognition.face_locations(imgS)
    enocodeCurFrame=face_recognition.face_encodings(imgS,faceCurFrame)
    
    imgBackground[162:162+480,55:55+640]=img
    imgBackground[44:44+633,808:808+414]=imgModeList[0]
    
    for encodeFace, faceLoc in zip(enocodeCurFrame,faceCurFrame):
        matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
        # print("matches",matches)
        # print("facedis",faceDis)
        matchIndex=np.argmin(faceDis)
        #print("MatchIndex", matchIndex)
        
        if matches[matchIndex]:
            # print("Known face detected")
            # print(studentIds[matchIndex])
            y1,x2,y2,x1=faceLoc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            bbox=55+x1,162+y1,x2-x1,y2-y1
            imgBackground=cvzone.cornerRect(imgBackground,bbox,rt=0)
    
    #cv2.imshow("Webcam",img)
    cv2.imshow("Face Attendance",imgBackground)
    cv2.waitKey(1)
