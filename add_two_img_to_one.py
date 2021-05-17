import cv2
import numpy as np

# 500 * 200
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

# 实际上 cv2 读进来的就是ndarray数据类型的，所以ndarray的方法、操作他都适用

# 这里的加法实际上仅仅是使用了矩阵运算，将两个矩阵的像素进行相加，加法结果未执行饱和加法
# add_img = img1 + img2
# print(add_img)

# 这里的加法综合了饱和度，像素叠加的上限设置为255
# (155,211,79) + (50, 170, 200) = 205, 381, 279=205，255，255这种情况下很容易使得图像过于白
# add_img = cv2.add(img1, img2)
# print(add_img)

# 为了避免像素溢出，我们可以使用带权重的 像素加法 addWeighted，该方法可以给每个图像设置一个权重再去完成相加计算
# 参数依次为 叠加的第一幅图像，像素权重，叠加的第二幅图片，像素权重，gamma是光谱值 给0就行
add_img = cv2.addWeighted(src1=img1, alpha=0.6, src2=img2, beta=0.4, gamma=0)

cv2.imshow('add img', add_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()


# 接下来演示如何通过图像处理操作叠加python logo到另一张图上，并且消除python logo的白色区域，不阻挡其他图片像素
# 最简单的思路是 直接用像素区域操作，替换这部分区域的像素即可，但是这样logo的白色会挡住原图的部分像素，因此我们要对这部分进行处理

img3 = cv2.imread('mainlogo.png')
# 由于想要将logo放到img1的左上角，因此需要知道logo的大小，以在img1中选择相等的区域
width, height, channels = img3.shape
print(width, height, channels)  # 126 126 3
# 接着在img1中节选出左上角与logo等大小的区域进行处理
roi = img1[0:width, 0:height]
# 接下来将logo图片转为灰度图，以便于后续进行像素二值化操作
img3_gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
# 使用阈值对灰度的logo图片进行二值化，thresh是阈值，maxval是当像素小于阈值时进行的操作值，具体怎么操作由type定，详见下一份代码
# ret就是输入参数的 thresh 值
# 这里的处理就是 对灰度的logo图片进行二值化，像素值大于220的点就变为255白色，否则全部变为黑色 0，logo为白色
ret, mask = cv2.threshold(img3_gray, thresh=220, maxval=255, type=cv2.THRESH_BINARY_INV)
# print(ret)
# bitwise_not对图像按位取反，灰度的二值logo图像 取反 的效果则是，黑色0变白255，白色255变黑0，logo为黑色
mask_inv = cv2.bitwise_not(mask)
# roi 是 一个三通道的图片，截取的img1左上角的图片，用它和 logo为黑色的mask_inv 按位置相与取较大值为结果，获得不被logo白色遮挡的roi区域
# 感觉这个效果就是 在mask的白色上面覆盖src的其他颜色，然后mask的黑色就依旧是黑色，生产的图片是以mask为主体的
# 将前景图logo变为黑色，其余背景变为白色，提取的roi 和 这个作and，相当于给 背景的白色部分绘制roi上的像素，
img1_bg = cv2.bitwise_and(src1=roi, src2=roi, mask=mask_inv)
# 因为mask的logo是白色的，其余都是黑色的，所以效果就是给logo上色，其余位置依旧保持黑色
# 大概意思就是提取出了前景图案，然后非前景图案都是黑色的，方便和背景图案进行像素求和，不干扰背景图效果
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)
# 将前景图和背景图 按照饱和度加法进行叠加，得到目标图案，img1的部分图案不会被logo的白色区域覆盖
dst = cv2.add(img3_fg, img1_bg)
# 将处理后的roi区域 覆盖 img1 的左上角，得到最终效果图
img1[0:width, 0:height] = dst

cv2.imshow('res', img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()