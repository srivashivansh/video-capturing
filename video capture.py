import cv2
import time

video = cv2.VideoCapture(0)

a= 1

while True:
    a = a+1
    check, frame = video.read()
    print(frame)
        
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert each frame into a gray scale image
        
    cv2.imshow("Capturing",gray)
        
    key = cv2.waitKey(1) #generate a new frame after every 1 miliseconds
        
    if key == ord('q'):  #once q is entered, window will be destroyed
        break

print(a) #this will print number of frames

video.release()

cv2.destroyAllWindows()
