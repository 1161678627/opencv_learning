'''
之前的模板匹配 template matching要求匹配模板 和待匹配的图像中的 目标完全相同，大小，反向，像素光线等等，条件太苛刻了
而特征匹配则是基于 图片像素之间的角点特征，首先提取模板中的特征，然后提取待匹配图片中的特征，来比较特征相似度完成匹配，
对模板和待匹配图中目标的相似度要求比较低，可以大小不同，方向不同等等               ->但似乎只能画出角点连线？
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('./opencv-feature-matching-image.jpg', 0)
img2 = cv2.imread('./opencv-feature-matching-template.jpg', flags=0)

# 创建ORB特征检测器和描述符
orb = cv2.ORB_create()

# 对两副图像检测特征和描述符
'''
keypoint 是一个包含若干点的列表
descriptor 对应每个点的描述符 是一个列表， 每一项都是检测到的特征的局部图像
检测的结果是关键点,计算的结果是描述符
可以根据监测点的描述符 来比较检测点的相似之处
'''
keypoint1, descriptor1 = orb.detectAndCompute(img1, None)
keypoint2, descriptor2 = orb.detectAndCompute(img2, None)

# 获得一个暴力匹配器对象
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# 利用匹配器，匹配两个描述符的相近程度
matches = bf.match(descriptor1, descriptor2)
# 按照匹配相近程度进行相似度排序，将相似度大的特征放到前面，优先使用相似度大的特征
matches = sorted(matches, key=lambda x: x.distance)

# 在两幅图上互标，画出匹配项，仅画前10项即可
img3 = cv2.drawMatches(img1, keypoint1, img2, keypoint2, matches1to2=matches[:10], outImg=None, flags=2)
plt.imshow(img3)
plt.show()
