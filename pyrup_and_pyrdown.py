'''
上采样：将图像进行放大方法的方法，会通过一些 规定的padding 填充方式将原始图像的像素数组进行放大，比如给每个像素附近填充0这种方式等等，采样后的图
会变得更大，但是也会变得更模糊，因为像素填充并不能使得图片变得更清晰，会损失一些精度
下采样：按照一定的方法将图像像素shape缩小，注意下采样出来的图片也会更加模糊，因为下采样也会导致精度损失的.
所以采样的过程实际上是，牺牲图片精度的过程，每使用一次，图片放大、缩小一倍，可以反复采样，也可以上下采样交替进行，如先上采样，再下采样，
这样虽然使得图片的大小没有改变，但是清晰度严重下降，因为图片像素信息丢失了两次。
'''
import cv2
import numpy as np

img = cv2.imread('./watch.jpg')
up = cv2.pyrUp(img)
down = cv2.pyrDown(img)
up_and_down = cv2.pyrDown(up)

dst = np.hstack((img, up_and_down))

cv2.imshow('up', up)
cv2.imshow('dowm', down)
cv2.imshow('original updown', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()