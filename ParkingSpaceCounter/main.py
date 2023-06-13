from cv2 import COLOR_RGB2GRAY
import numpy
import cv2
import pickle
import cvzone

cap=cv2.VideoCapture('D:\Computer vision\ParkingSpaceCounter\carPark.mp4')

w,h=48,107

with open('D:\Computer vision\ParkingSpaceCounter\CarParkPos','rb') as f:
    PosList=pickle.load(f)

def carParCheck(image):
    for pos in PosList:
        spaceCounter=0
        x,y=pos
        imgCrop=image[y:y+w,x:x+h]
        # cv2.imshow('image',parkingSpace)
        # cv2.waitKey()

        count = cv2.countNonZero(imgCrop)
        if count < 700:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
             color = (0, 0, 255)
             thickness = 2

        cv2.rectangle(frame, pos, (pos[0] + h, pos[1] + w), color, thickness)
        # cvzone.putTextRect(frame, str(count), (x, y + h - 3), scale=1,
        #                 thickness=2, offset=0, colorR=color)

while(True):
    ret,frame=cap.read()
    if ret:
        grayFrame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
        imgThreshold = cv2.adaptiveThreshold(grayFrame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
        carParCheck(imgThreshold)
        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cv2.destroyAllWindows()

# ret,frame=cap.read()
# cv2.imwrite('farme.png',frame)