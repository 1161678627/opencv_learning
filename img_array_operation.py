import cv2
import numpy as np

img = cv2.imread('./watch.jpg')

# 这个img实际上就是一个ndarray对象，任何符合numpy的操作都可以对他进行，只不过物理意义是像素点
# 选择roi时，是先选择垂直方向，再选择水平方向的

# 选定图片上某个点的像素
px = img[55, 55]
print(px)  # [29 31 42] 输出的是一个 bgr 三通道像素颜色数值

# 修改图片上某个点的像素
img[55, 55] = [255, 255, 255]

# 如果是灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray_img[55, 55])  # 则返回单通道 数字 255

# 当然以上操作也可以对某个区域整体进行
img[20:100, 20:100] = [255, 0, 0]

watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 循环遍历整个图片所有像素
height, width, channel = img.shape
for i in range(height):
    for j in range(width):
        val_R = img[i, j, 2]
        val_G = img[i, j, 1]
        val_B = img[i, j, 0]