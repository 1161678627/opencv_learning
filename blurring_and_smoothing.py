import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
while ret:
    cv2.imshow('original', frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_ = np.array([10, 180, 160])
    upper_ = np.array([25, 255, 180])
    mask = cv2.inRange(src=hsv, lowerb=lower_, upperb=upper_)
    # 颜色过滤后的原图，这里一定要用mask传进去mask参数
    dst = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('dst', dst)

    # averaging smothing 平均平滑, 255 = 15*15,一般都具有这个关系，取平均
    kernel = np.ones(shape=(5, 5), dtype=np.float32)/25
    # 实际上是利用15*15的卷积核对原图进行平均卷积操作实现的平滑，kernel为卷积核
    averaging_smoothed = cv2.filter2D(src=dst, ddepth=-1, kernel=kernel)
    cv2.imshow('averaging smoothed', averaging_smoothed)

    # 高斯平滑，ksize为 高斯核大小
    gauss_blur = cv2.GaussianBlur(src=dst, ksize=(5, 5), sigmaX=0)
    cv2.imshow('Gaussian Blurring', gauss_blur)

    # 中值模糊，卷积核的大小应该为奇数，使用卷积框像素的中值来代替这部分像素值
    median_blur = cv2.medianBlur(src=dst, ksize=5)
    cv2.imshow('Median Blur', median_blur)

    # 双边模糊，#15 邻域直径，两个 75 分别是空间高斯函数标准差，灰度值相似性高斯函数标准差，速度较慢
    # 它的特点是 能够在平滑源图像时，依旧保持源图像的边界清晰，不会连边界一起平滑掉
    bilateral_blur = cv2.bilateralFilter(dst, 15, 75, 75)
    cv2.imshow('bilateral Blur', bilateral_blur)

    key = cv2.waitKey(5)
    if key & 0xFF == 27:
        break

    ret, frame = cap.read()

cap.release()
cv2.destroyAllWindows()