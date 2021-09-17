import cv2
import numpy as np

img = cv2.imread("./cards.jpg")

# 仿射变换，将形状扭曲的矩形图案，映射为正规矩形
# King
# 首先定义两个点集，src表示 扭曲图案在原图上的四个坐标点，dst表示映射后的新img上对应的四个坐标点
# 因为中间要计算变换矩阵，会有除法计算，且cv2底层是c++，存在小数点截取问题，因此定义为np.float32
src = np.float32([[529, 142], [771, 190], [405, 395], [674, 457]])
# 定义目标矩形的size
w = 250
h = 350
dst = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
matrix = cv2.getPerspectiveTransform(src, dst)
# dsize 为定义目标矩形的size
imgWarp = cv2.warpPerspective(img, matrix, (w, h))

cv2.imshow('img', img)
cv2.imshow('imgWarp', imgWarp)
cv2.waitKey(0)