import numpy as np
import cv2

# 更多详细的关于 前景提取，背景消除的 案例见 https://www.jianshu.com/p/a8a9bc22ebca

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    fgmask = fgbg.apply(frame)
    cv2.imshow('original', frame)
    cv2.imshow('mog background reduction', fgmask)
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()