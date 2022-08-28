import cv2
import math
goalx=530
goaly=300
video=cv2.VideoCapture('bb3.mp4')
tracker=cv2.TrackerCSRT_create()
ret,image = video.read()
bbox=cv2.selectROI("tracking",image,True)
tracker.init(image,bbox)
def drawboundrybox(image,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(image,(x,y),(x+w,y+h),3,3)
def goaltracking(image,bbox):
     x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
     c1=x+int(w/2)
     c2=y+int(h/2)
     cv2.circle(image,(c1,c2),3,(0,0,0),3)
     cv2.circle(image,(goalx,goaly),3,(0,0,0),3)
     dist = math.sqrt(((c1-goalx)**2) + (c2-goaly)**2)
     if dist<40:
            cv2.putText(image,"Goal Achived",(350,90),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,0.9,(0,0,0))





while True:
    ret,image = video.read()
    success,bbox=tracker.update(image)
    if success==True:
        drawboundrybox(image,bbox)
    goaltracking(image,bbox)
    cv2.imshow("result",image)
    if cv2.waitKey(1)==32:
        break
cv2.destroyAllWindows()







