import cv2
import numpy as np

img = cv2.imread('./watch.jpg')

# 这个img实际上就是一个ndarray对象，任何符合numpy的操作都可以对他进行，只不过物理意义是像素点
# 选择roi时，是先选择垂直方向，再选择水平方向的

# 选定图片上某个点的像素
px = img[55, 55]
print(px)  # [29 31 42] 输出的是一个 bgr 三通道像素颜色数值

# 修改图片上某个点的像素，三通道图片就要传入三通道的 颜色rgb值才能修改成功
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

# 图片bgr像素通道分离
b, g, r = cv2.split(img)
print(r)

# 图片像素分离还可以通过 ndarray的 索引操作完成  b g r ->0 1 2
# 此时分离的是一个 单通道的 像素数组，修改某个位置的像素值时，仅需要 赋值 “标量数字” 即可。
r = img[:, :, 2]
print(r)

# 图片像素通道融合
img2 = cv2.merge((b, g, r))

# 给图片填充 上下左右 边框区域， padding操作
# 先指定 给图片要填充的   边界区域的大小，顺序为 上下左右
top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)
# borderType 取不同的值表示不同的填充方式，取常值就会填充固定像素
dst = cv2.copyMakeBorder(src=img, top=top_size, bottom=bottom_size, left=left_size, right=right_size, borderType=0)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 由于cv2读取的图片像素数组的取值范围都是 uint8的 0-255范围的 像素数值.
# 因此，当执行矩阵运算，使得运算结果范围超过255时，就会自动对 运算结果 取余截断到255范围之内，从而使得可视化计算结果时，可视化结果失去意义
# 矩阵运算 指 没有使用cv2 完成的 像素矩阵 加减乘除 操作
img3 = img + img2
print(img3[:20, :, 0])

# 但是如果使用cv2.add 之类的 cv2自带的 图像处理api去做，就会不一样，cv2 的add会当相加加过大于255时，输出255作为最终结果而不是取余
print(cv2.add(img, img2)[:20, :, 0])