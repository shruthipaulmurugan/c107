import cv2
import time
import math

p1 = 530
p2 = 300
xs = []
ys = []

video = cv2.VideoCapture("bb3.mp4")
tracker = cv2.TrackerCSRT_create()
returned, img = video.read()
bbox = cv2.selectROI("tracking", img, False)
tracker.init(img, bbox)
print(bbox)
def drawbox(img, bbox):
    x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x,y), (x+w), (y+h), (255,0,255), 3, 1)
    cv2.PutText(img, "tracking", (75, 90), cv2.FONT_HERSHEY_SiMPLEX, 0.7, (0, 255, 0), 2)

def goal_track(img, bbox):
    x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    c1 = x+int(w/2)
    c2 = y+int(h/2)
    cv2.circle(img, (c1, c2), 2, (0,0,255), 5)
    dist = math.sqrt(((c1-p1)**2)+(c2-p2)**2)
    print(dist)

while True:
    check,img = video.read()   

    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()



