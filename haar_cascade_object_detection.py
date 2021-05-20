import cv2

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    '''
    scaleFactor表示每次图像尺寸减小的比例
    minNeighbors表示每一个目标至少要被检测到3次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸),
    返回值是这样一个数组，分别是每个人脸的 x,y,w,h坐标  xy是左上坐标
    [[ 60  11 156 156]
    [439 247 190 190]]
    '''
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    # print(faces)
    for x, y, w, h in faces:
        cv2.rectangle(img=frame, pt1=(x, y), pt2=(x+w, y+h), color=(0, 0, 255), thickness=2)
        roi_gray = gray[y:y+h, x:x+w]   # 注意opencv在截取roi时，是先竖着截height再横着截width的
        # roi_color 是从 frame取出来的局部，对roi_color进行修改，如画矩形，frame 也会收到影响，在对应区域出现矩形的，不完全拷贝
        roi_color = frame[y:y+h, x:x+w]  # 注意opencv在截取roi时，是先竖着截height再横着截width的
        # 这里检测眼睛的思路是，从检测到的脸上进一步检测眼睛，提高眼睛检测的健壮性
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=1)
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), color=(0, 255, 0), thickness=2)

    cv2.imshow('dst', frame)
    key = cv2.waitKey(5) & 0xff
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()