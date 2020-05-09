#There will different task perform on click of diffrent mouse button
#Import diffrent library of python.Here CV2(open cv) library for image processing and numpy for array manuplation.
import cv2
import numpy as np
def nothing(x):
    pass
#create a 300X700 size window of black color
img = np.zeros((300,700,3),np.uint8)
#Declearing window name
cv2.namedWindow('image')
#create diffrent trackbar on window with value range 0-255 whic is RGB range
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
#switch trackbar
switch ='0:OFF  1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

while True:
    # show created image on window
    cv2.imshow('image',img)
    # exit if Enter Key is press
    if cv2.waitKey(1)==13:
        break
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    #check switch value
    if s==0:
        img[:]=0
    else:
        img[:] = [b,g,r]
cv2.destroyAllWindows()