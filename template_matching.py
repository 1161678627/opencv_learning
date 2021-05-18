import cv2
import numpy as np

# 先读取一个彩色版本，展示的时候在彩色版本展示匹配效果
img_bgr = cv2.imread('./opencv-template-matching-python-tutorial.jpg')
# 再处理一个灰度版本，匹配的操作在灰度版本上进行
img_gray = cv2.cvtColor(img_bgr, code=cv2.COLOR_BGR2GRAY)

# 直接读取灰度版本，用于匹配过程
template = cv2.imread('./opencv-template-for-matching.jpg', flags=0)
width, height = template.shape

# 模板就是一副已知的小图像，而模板匹配就是在一副大图像中搜寻目标，已知该图中有要找的目标，且该目标同模板有相同的尺寸、方向和图像元素
# method指用于匹配相同图像的算法，TM_CCOEFF_NORMED是利用相似度计算的，效果比较好，但是耗费计算资源，转为灰度图片，可以减少耗时
# 这个匹配感觉像是 不断的移动模板，然后匹配出可能相似的 左上点坐标，和相似度概率，所以一个目标，有可能会偏移几个像素点然后同时匹配多次
# 匹配的结果可能就差一个像素，但是置信度都很高，所以画线的时候就会 画的比较厚实
# matchTemplate可以对彩色/灰度图像进行匹配
res = cv2.matchTemplate(image=img_gray, templ=template, method=cv2.TM_CCOEFF_NORMED)
# 设定阈值，只有当匹配置信度在这个阈值以上的才认为 匹配成功,阈值大就会匹配的少而准，小就会匹配的多而错，就是召回率和准确率的考量了
threshold = 0.8
loc = np.where(res > threshold)
print(loc)
# 可能匹配多个目标的固定写法，如果是确定只有一个目标可以用 minMaxLoc 函数处理，从loc中遍历得到的左上坐标 pt -> (10, 10)
for pt in zip(*loc[::-1]):
    # 指定左上和右下坐标 画矩形
    cv2.rectangle(img_bgr, pt, (pt[0]+width, pt[1]+height), color=(0, 0, 255), thickness=2)

cv2.imshow('Detected', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()