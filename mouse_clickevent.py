#There will different task perform on click of diffrent mouse button
#Import diffrent library of python.Here CV2(open cv) library for image processing and numpy for array manuplation.
import cv2
import numpy as np
#Declearing window name
windowname = 'drawing'
#create a 300X512 size window of black color
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow(windowname)
 #Mouse call back function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(0,255,0),-1)
    if event == cv2.EVENT_MBUTTONDOWN:
        cv2.circle(img,(x,y),15,(0,0,255),-1)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),20,(255,0,0),-1)

#On clicking mouse call draw_circle function on window name as windowname
cv2.setMouseCallback(windowname,draw_circle)
while True:
    #show created image on window
     cv2.imshow(windowname,img)
    #exit if Enter Key is press
     if cv2.waitKey(1)==13:
         break
cv2.destroyAllWindows()

