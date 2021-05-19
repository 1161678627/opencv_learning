import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./WIN_20210518_20_18_16_Pro.jpg')
# 生成一个与原图等大小的掩码图片，固定写法
mask = np.zeros(shape=img.shape[:2], dtype=np.uint8)

# 定义前景模型和背景模型，固定写法
fgdmodel = np.zeros(shape=(1, 65), dtype=np.float64)
bgdmodel = np.zeros(shape=(1, 65), dtype=np.float64)

# 定义要抠图的区域，包含前景的矩形，格式为 (x,y,w,h) 左上点的xy，该区域的w，h
rect = (230, 1, 295, 357)

# 开始提取前景，前5个参数基本都是固定写法，iterCount指迭代的次数，因为我们用rect定义前景区域，所以mode就是GC_INIT_WITH_RECT
# rect 用于限定需要进行分割的图像范围，只有该矩形窗口内的图像部分才被提取前景；
# 处理后的结果会保存在mask矩阵中->即mask矩阵会被修改，img啥的都不变，所以下面我们调用mask就行
cv2.grabCut(img, mask, rect, bgdmodel, fgdmodel, iterCount=1, mode=cv2.GC_INIT_WITH_RECT)

'''
处理后的mask取值如下：
GCD_BGD（=0），背景；
GCD_FGD（=1），前景；
GCD_PR_BGD（=2），可能的背景；
GCD_PR_FGD（=3），可能的前景。
'''
# 我们给mask中值为0/2->背景 的赋值0，其余1/3 ->前景 赋值1
# np.where 当符合条件时是x，不符合是y，常用于根据一个数组产生另一个新的数组。
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# 然后利用矩阵乘法，把处理后的mask2，即只有前景区域值为1，其余区域值都为0的像素，和原图矩阵相乘，结果就是 原图中背景区域全为0，黑色，前景区域不变
# 矩阵相乘保持通道数一致
grabcut = img*mask2[:, :, np.newaxis]

cv2.imshow('original', img)
cv2.imshow('grabcut', grabcut)
plt.imshow(grabcut)
plt.colorbar()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()