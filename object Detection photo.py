import cv2

img = cv2.imread('abc.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

flag,frame = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

res,h = cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

cv2.imshow('ORIGINAL IMG',img)


img2 = cv2.drawContours(img,res,-1,(0,0,0),3)

cv2.imshow('RESULT',img2)


cv2.waitKey(0)
cv2.destroyAllWindows()