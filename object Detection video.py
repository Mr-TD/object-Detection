import cv2
vid = cv2.VideoCapture(0)
flag, fream1 = vid.read()
flag, fream2 = vid.read()
while True:
    diff = cv2.absdiff(fream1, fream2)
    vid2 = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    vid3 = cv2.GaussianBlur(vid2, (35,35), 0)
    flag1, frame3 = cv2.threshold(vid3, 30, 255, cv2.THRESH_BINARY)
    cotures, frame4 = cv2.findContours(frame3, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for c in cotures:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(fream1, (x, y), ((x + w), (y + h)), (0, 255, 0), 2)



        # print(cvt)
    # cv2.drawContours(fream1, cotures, -1, (0, 0, 255), 2)
    cv2.imshow("Video", fream1)
    cv2.imshow("VIDEO2", frame3)
    fream1 = fream2
    flag,fream2 = vid.read()
    cv2.waitKey(100)
vid.release()
cv2.destroyAllWindows()