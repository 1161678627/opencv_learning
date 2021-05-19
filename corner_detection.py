import numpy as np
import cv2

img = cv2.imread('./opencv-corner-detection-sample.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 因为goodFeaturesToTrack接受的图像是 单通道 float32类型的，因此需要做如下转换
gray_img = gray_img.astype(np.float32)
print(gray_img.dtype)

'''
image: 输入图像，是八位的或者32位浮点型，单通道图像，所以有时候用灰度图
maxCorners: 返回最大的角点数，是最有可能的角点数，如果这个参数不大于0，那么表示没有角点数的限制。
qualityLevel: 图像角点的最小可接受参数，质量测量值乘以这个参数就是最小特征值，小于这个数的会被抛弃。
minDistance: 返回的角点之间最小的欧式距离。
mask: 检测区域。如果图像不是空的(它需要具有CV_8UC1类型和与图像相同的大小)，它指定检测角的区域。
blockSize: 用于计算每个像素邻域上的导数协变矩阵的平均块的大小。
useHarrisDetector：选择是否采用Harris角点检测，默认是false.
k: Harris检测的自由参数。

返回的corners是float类型的x y 角点坐标对，需要转换为 int类型，方便在原图绘制
'''
corners = cv2.goodFeaturesToTrack(image=gray_img, maxCorners=100, qualityLevel=0.01, minDistance=10)
print('转换前', corners)
corners = corners.astype(np.int0)
print('转换后', corners)

for corner in corners:
    x, y = corner.ravel()
    # thickness -1 表示填充圆形
    cv2.circle(img, center=(x, y), radius=3, color=(0, 255, 255), thickness=-1)

cv2.imshow('goodFeaturesToTrack', img)
cv2.waitKey(0)
cv2.destroyAllWindows()