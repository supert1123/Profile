import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
prevframe = frame    #First frame
while True:
    ret, frame = cap.read()
    nextframe = frame
    if ret:
        diff = cv2.absdiff(prevframe,nextframe)
        cv2.imshow('video', diff)
        prevframe = nextframe   #Frame difference method Background change
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
cv2.destroyAllWindows()
cap.release()