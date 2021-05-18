import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, code=cv2.COLOR_BGR2HSV)
    lower_ = np.array([10, 180, 160])
    upper_ = np.array([25, 255, 180])
    mask = cv2.inRange(hsv, lowerb=lower_, upperb=upper_)
    # dst = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('mask', mask)

    kernal = np.ones((5, 5), dtype=np.uint8)
    # 膨胀操作，增加图像中的白色区域，或者链接两个分开的区域，iterations指迭代的次数，次数越大效果越明显
    dilation = cv2.dilate(src=mask, kernel=kernal, iterations=1)
    cv2.imshow('dilation', dilation)

    # 腐蚀操作，去掉白色噪声，断开两个连接在一起的物体
    erosion = cv2.erode(mask, kernal, iterations=1)
    cv2.imshow('erosion', erosion)

    # 开操作，先腐蚀再膨胀，用来去除白色噪声
    opening = cv2.morphologyEx(mask, op=cv2.MORPH_OPEN, kernel=kernal, iterations=1)
    # 闭操作，先膨胀再腐蚀，用于填充黑色小洞
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal, iterations=1)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()