import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 注意边缘检测可以对彩色图像进行,
    # Laplacian算子
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    # sobel算子，dx，dy表示求导的深度，0不求导，1求一阶导，2求二阶导，ksize是Sobel算子的大小，必须为奇数
    sobelx = cv2.Sobel(frame, cv2.CV_64F, dx=1, dy=0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, dx=0, dy=1, ksize=5)

    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)


    # canny边缘检测，也可以对彩色图像进行，也可以对灰度图像进行
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 高斯滤波能够滤除图像中的高频信息，能够消除高频的噪声对边缘检测的影响，所以有时可以先加个高斯滤波再去canny边缘检测
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    # 参数依次为，阈值1，阈值2，其中较大的阈值2用于检测图像中明显的边缘，但一般情况下检测的效果不会那么完美，边缘检测出来是断断续续的。
    # 所以这时候用较小的第一个阈值用于将这些间断的边缘连接起来。
    canny_edge = cv2.Canny(frame, threshold1=50, threshold2=100)
    cv2.imshow('canny edge', canny_edge)

    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()