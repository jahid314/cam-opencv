import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
print("check ==",cap.isOpened())
fourcc=cv2.VideoWriter_fourcc(*"CVID")
output=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame=cv2.flip(frame,1)
        output.write(gray)
        cv2.imshow("grayframe",gray)
        cv2.imshow("color frame",frame)
        if cv2.waitKey(0)&0xFF == ord("q"):
            break
        else:
            break
        cap.release()
        output.release()
        cv2.destroyAllWindows()
            