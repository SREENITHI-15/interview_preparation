import cv2


def trackChaned(x):
  pass
 


cv2.namedWindow('Color Track Bar')
hh='Max'
hl='Min'
wnd = 'Colorbars'
cv2.createTrackbar("Max", "Color Track Bar",0,255,trackChaned)
cv2.createTrackbar("Min", "Color Track Bar",0,255,trackChaned) 
cv2.createTrackbar("Max1", "Color Track Bar",0,255,trackChaned)
cv2.createTrackbar("Min1", "Color Track Bar",0,255,trackChaned)
img = cv2.imread('dog.jpg')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



while(True):
   hul=cv2.getTrackbarPos("Max", "Color Track Bar")
   huh=cv2.getTrackbarPos("Min", "Color Track Bar")
   ret,thresh1 = cv2.threshold(img,hul,huh,cv2.THRESH_BINARY) 
   hul1=cv2.getTrackbarPos("Max1", "Color Track Bar")
   huh1=cv2.getTrackbarPos("Min1", "Color Track Bar")
   ret,thresh4 = cv2.threshold(img,hul1,huh1,cv2.THRESH_BINARY_INV)
   cv2.imshow("thresh1",thresh1)
   cv2.imshow("thresh4",thresh4)
   if cv2.waitKey(1) == 27:
       break
cv2.destroyAllWindows()