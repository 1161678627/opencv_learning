import cv2
from copy import deepcopy
import numpy as np

img = cv2.imread('./watch.jpg')
# img_ = deepcopy(img)  # 需要深度拷贝才能保留原来图层不被修改

'p.s. cv2的坐标系从左上开始（0，0）'

# 画线函数，虽然有返回值，但是传入的img像素点也被修改了，因此我们直接用img当作绘制完的图就可以了，不去写返回值
# 参数依次为 传入的图片，直线起始点，直线结束点，线条颜色，线条宽度
cv2.line(img, (0, 0), (150, 150), color=(255, 255, 255), thickness=15)

# 画矩形，参数依次为 传入的图片，矩形左上，矩形右下点，线条颜色，线条宽度
# 当 线宽thickness 取-1表示填充，默认取 1
cv2.rectangle(img, (10, 10), (50, 50), color=(255, 0, 0), thickness=-1)

# 画圆,参数依次为 图片，圆心，半径，颜色
cv2.circle(img, center=(60, 60), radius=30, color=(0, 255, 0))

# 画椭圆，参数依次为 图片，中心点位置，长轴和短轴的长度，椭圆沿逆时针选择角度，椭圆沿顺时针方向起始角度,和结束角度
cv2.ellipse(img, center=(70, 70), axes=(100, 50), angle=0, startAngle=0, endAngle=180, color=(0, 0, 255), thickness=-1)

# 画多边形，
pts = np.array([[10, 3], [48, 19], [60, 3], [98, 19]], np.int32)  # 数据类型必须是int32
print(pts.shape)
print(pts)
# 这里 reshape 的第一个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的。 要求的维度比较奇怪，就模拟这种写法吧
pts = pts.reshape((-1, 1, 2))
print(pts.shape)
print(pts)
# 参数依次为 图像，点集，是否闭合，颜色
cv2.polylines(img, [pts], isClosed=True, color=(255, 0, 255))

# 写文字,首先指定一种字体格式,默认的字体只能展示英文字符
font = cv2.FONT_HERSHEY_SIMPLEX
# 参数依次为 图像，绘制的文字，位置，字型，字体大小，文字颜色，线型
cv2.putText(img, 'opencv', (100, 120), font, 2, color=(255, 0, 0), thickness=3)

cv2.imshow('watch img', img)
cv2.waitKey()

cv2.destroyAllWindows()
