import numpy as np
import cv2
video=cv2.VideoCapture("CarParkProject/carPark.mp4")
ret, Prev_frame= video.read()
ret, Current_frame=video.read()
while video.isOpened():

    frame_diff= cv2.absdiff(Current_frame, Prev_frame)
    imgray = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(imgray, (5,5), 0)
    ret, thresh = cv2.threshold(blur, 16, 255, cv2.THRESH_BINARY)
    canny=cv2.Canny(Prev_frame, 100, 200)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 
    cv2.drawContours(canny, contours, -1, (255, 255, 255), 2)
    #cv2.drawContours(Prev_frame, contours, -1, (255, 255, 255), 1)
    gray=cv2.cvtColor(Prev_frame, cv2.COLOR_BGR2GRAY)
    #first one
    for i in range(1):

        r=0*50
        
        modifiedImage = canny[436-r:472-r, 164-120:259-120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,255,0), 2)
    for i in range(1):

        r=1*50
        
        modifiedImage = canny[436-r:472-r, 164-120:259-120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,255,0), 2)
    for i in range(1):

        r=2*50
        
        modifiedImage = canny[436-r:472-r, 164-120:259-120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,255,0), 2)
    for i in range(1):

        r=3*50
        
        modifiedImage = canny[436-r:472-r, 164-120:259-120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,255,0), 2)
    for i in range(1):

        r=4*50
        
        modifiedImage = canny[436-r:472-r, 164-120:259-120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,255,0), 2)
    for i in range(1):

        r=5*50
        
        modifiedImage = canny[436-r:472-r, 164-120:259-120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,255,0), 2)
    for i in range(1):

        r=6*50
        
        modifiedImage = canny[436-r:472-r, 164-120:259-120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,255,0), 2)
    for i in range(1):

        r=7*50
        
        modifiedImage = canny[436-r:472-r, 164-120:259-120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=200:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,0,255), 2)
        elif nowp<200:
            cv2.rectangle(Prev_frame, (164-120,436-r), (259-120,472-r), (0,255,0), 2)
    for i in range(1):

        r=1*50
        
        modifiedImage = canny[436+r:472+r, 164-120:259-120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164-120,436+r), (259-120,472+r), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164-120,436+r), (259-120,472+r), (0,255,0), 2)
    for i in range(1):

        r=2*50
        
        modifiedImage = canny[436+r:472+r, 164-120:259-120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164-120,436+r), (259-120,472+r), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164-120,436+r), (259-120,472+r), (0,255,0), 2)
    for i in range(1):

        r=3*50
        
        modifiedImage = canny[436+r:472+r, 164-120:259-120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164-120,436+r), (259-120,472+r), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164-120,436+r), (259-120,472+r), (0,255,0), 2)
    for i in range(1):

        r=4*50
        
        modifiedImage = canny[436+r:472+r, 164-120:259-120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164-120,436+r), (259-120,472+r), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164-120,436+r), (259-120,472+r), (0,255,0), 2)
    #2nd one
    for i in range(1):

        r=7*50
        
        modifiedImage = canny[436-r:472-r, 164:259]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=900:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,0,255), 2)
        elif nowp<900:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,255,0), 2)
    for i in range(1):

        r=6*50
        
        modifiedImage = canny[436-r:472-r, 164:259]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,255,0), 2)
    for i in range(1):

        r=5*50
        
        modifiedImage = canny[436-r:472-r, 164:259]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,255,0), 2)
    for i in range(1):

        r=4*50
        
        modifiedImage = canny[436-r:472-r, 164:259]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,255,0), 2)
    for i in range(1):

        r=3*50
        
        modifiedImage = canny[436-r:472-r, 164:259]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,255,0), 2)
    for i in range(1):

        r=2*50
        
        modifiedImage = canny[436-r:472-r, 164:259]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,255,0), 2)
    for i in range(1):

        r=1*50
        
        modifiedImage = canny[436-r:472-r, 164:259]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164,436-r), (259,472-r), (0,255,0), 2)  
    #below this is the origin.
    for i in range(1):

        r=0*50
        
        modifiedImage = canny[436:472, 164:259]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164,436), (259,472), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164,436), (259,472), (0,255,0), 2)
    for i in range(1):

        r=1*50
        
        modifiedImage = canny[436+r:472+r, 164:259]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164,436+r), (259,472+r), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164,436+r), (259,472+r), (0,255,0), 2)  
    for i in range(1):

        r=2*50
        
        modifiedImage = canny[436+r:472+r, 164:259]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164,436+r), (259,472+r), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164,436+r), (259,472+r), (0,255,0), 2)  
    for i in range(1):

        r=3*50
        
        modifiedImage = canny[436+r:472+r, 164:259]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164,436+r), (259,472+r), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164,436+r), (259,472+r), (0,255,0), 2)  
    for i in range(1):

        r=4*50
        
        modifiedImage = canny[436+r:472+r, 164:259]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164,436+r), (259,472+r), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164,436+r), (259,472+r), (0,255,0), 2)  
    #3rd one
    for i in range(1):

        r=0*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230:259+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230,436+r-10), (259+230,472+r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230,436+r-10), (259+230,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=1*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230:259+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230,436+r-10), (259+230,472+r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230,436+r-10), (259+230,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=2*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230:259+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230,436+r-10), (259+230,472+r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230,436+r-10), (259+230,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=3*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230:259+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230,436+r-10), (259+230,472+r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230,436+r-10), (259+230,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=4*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230:259+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230,436+r-10), (259+230,472+r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230,436+r-10), (259+230,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=1*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230:259+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230,436-r-10), (259+230,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230,436-r-10), (259+230,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=2*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230:259+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230,436-r-10), (259+230,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230,436-r-10), (259+230,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=3*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230:259+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230,436-r-10), (259+230,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230,436-r-10), (259+230,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=4*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230:259+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230,436-r-10), (259+230,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230,436-r-10), (259+230,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=5*50
        
        modifiedImage = canny[436-r:472-r, 164+230:259+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1100:
            cv2.rectangle(Prev_frame, (164+230,436-r), (259+230,472-r), (0,0,255), 2)
        elif nowp<1100:
            cv2.rectangle(Prev_frame, (164+230,436-r), (259+230,472-r), (0,255,0), 2)
    for i in range(1):

        r=6*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230:259+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230,436-r-10), (259+230,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230,436-r-10), (259+230,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=7*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230:259+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230,436-r-10), (259+230,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230,436-r-10), (259+230,472-r-10), (0,255,0), 2)
#fourth one
    for i in range(1):

        r=0*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120:259+230+120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=1*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120:259+230+120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=2*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120:259+230+120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=3*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120:259+230+120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=4*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120:259+230+120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=5*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120:259+230+120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=6*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120:259+230+120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=7*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120:259+230+120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230+120,436-r-10), (259+230+120,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=1*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230+120:259+230+120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164+230+120,436+r-10), (259+230+120,472+r-10), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164+230+120,436+r-10), (259+230+120,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=2*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230+120:259+230+120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230+120,436+r-10), (259+230+120,472+r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230+120,436+r-10), (259+230+120,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=3*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230+120:259+230+120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230+120,436+r-10), (259+230+120,472+r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230+120,436+r-10), (259+230+120,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=4*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230+120:259+230+120]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230+120,436+r-10), (259+230+120,472+r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230+120,436+r-10), (259+230+120,472+r-10), (0,255,0), 2)
#5th one
    for i in range(1):

        r=0*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230+120+230:259+230+120+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436+r-10), (259+230+120+230,472+r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436+r-10), (259+230+120+230,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=1*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230+120+230:259+230+120+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=500:
            cv2.rectangle(Prev_frame, (164+230+120+230,436+r-10), (259+230+120+230,472+r-10), (0,0,255), 2)
        elif nowp<500:
            cv2.rectangle(Prev_frame, (164+230+120+230,436+r-10), (259+230+120+230,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=2*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230+120+230:259+230+120+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436+r-10), (259+230+120+230,472+r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436+r-10), (259+230+120+230,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=3*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230+120+230:259+230+120+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436+r-10), (259+230+120+230,472+r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436+r-10), (259+230+120+230,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=4*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230+120+230:259+230+120+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436+r-10), (259+230+120+230,472+r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436+r-10), (259+230+120+230,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=1*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230:259+230+120+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=2*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230:259+230+120+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=1000:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,0,255), 2)
        elif nowp<1000:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=3*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230:259+230+120+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=4*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230:259+230+120+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=5*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230:259+230+120+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=6*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230:259+230+120+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=7*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230:259+230+120+230]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230,436-r-10), (259+230+120+230,472-r-10), (0,255,0), 2)   
#last one
    for i in range(1):

        r=0*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230+155:259+230+120+230+155]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,255,0), 2)    
    for i in range(1):

        r=1*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230+155:259+230+120+230+155]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=2*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230+155:259+230+120+230+155]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=3*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230+155:259+230+120+230+155]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=4*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230+155:259+230+120+230+155]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=5*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230+155:259+230+120+230+155]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=6*50
        
        modifiedImage = canny[436-r-10:472-r-10, 164+230+120+230+155:259+230+120+230+155]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436-r-10), (259+230+120+230+155,472-r-10), (0,255,0), 2)
    for i in range(1):

        r=1*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230+120+230+155:259+230+120+230+155]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436+r-10), (259+230+120+230+155,472+r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436+r-10), (259+230+120+230+155,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=2*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230+120+230+155:259+230+120+230+155]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436+r-10), (259+230+120+230+155,472+r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436+r-10), (259+230+120+230+155,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=3*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230+120+230+155:259+230+120+230+155]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436+r-10), (259+230+120+230+155,472+r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436+r-10), (259+230+120+230+155,472+r-10), (0,255,0), 2)
    for i in range(1):

        r=4*50
        
        modifiedImage = canny[436+r-10:472+r-10, 164+230+120+230+155:259+230+120+230+155]
        nowp = np.sum(modifiedImage == 255)
        if nowp>=400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436+r-10), (259+230+120+230+155,472+r-10), (0,0,255), 2)
        elif nowp<400:
            cv2.rectangle(Prev_frame, (164+230+120+230+155,436+r-10), (259+230+120+230+155,472+r-10), (0,255,0), 2)
    
    print(nowp)
    cv2.imshow("Absolute Diff",Prev_frame)
    Prev_frame=Current_frame
    ret, Current_frame=video.read()
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
