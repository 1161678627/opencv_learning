import cv2

img = cv2.imread('./bookpage.jpg')

# 固定阈值二值化，参数依次为 源图像，设定的固定阈值，当像素值超过了阈值（或者小于阈值，根据type来决定）所赋予的值，二值化操作的类型
# 一般src常为灰度图片，然后对其进行二值化，但请注意阈值化不一定非要传入灰度图片，如果是彩色图片，则处理结果为三通道的 0/255 的三通道像素
# ret为设定的 thresh值，一般用不到
'''
type包含以下5种类型:
cv2.THRESH_BINARY :比thresh大的赋值maxval，比thresh小的赋值0——简单说就是亮的更亮，暗的更暗
cv2.THRESH_BINARY_INV ：比thresh小的赋值maxval，比thresh大的赋值0——简单说就是亮的变暗，暗的变亮的取反
cv2.THRESH_TRUNC ：比thresh大的赋值maxval，比thresh小的不变
cv2.THRESH_TOZERO ：比thresh大的不变，比thresh小的变黑——和maxval的值无关？
cv2.THRESH_TOZERO_INV ：比thresh大的变黑，比thresh小的不变——和maxval的值无关？
'''
# 所以这里实现的效果就是大于12的像素点 变255，其余都变0，暗的更暗，亮的更亮，看得清字体
ret, threshold = cv2.threshold(src=img, thresh=12, maxval=255, type=cv2.THRESH_BINARY)
print(ret)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 对灰度图片进行 固定阈值二值化
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(src=img_gray, thresh=12, maxval=255, type=cv2.THRESH_BINARY)
cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 对灰度图片进行自适应阈值二值化,将大图分为好多个子块，每个子块自动选一个阈值出来，这种分治使得每个子块的阈值都能更好的区分该子块中的图像差异
# 参数和threshold中的基本相同，着重说下adaptiveMethod是 给每个子块 自适应选择 合适阈值的方法，blockSize是每个子块划分的大小，C是计算阈值时的常数项
'''
adaptiveMethod一共有两种选择，一般都选高斯：
cv2.ADAPTIVE_THRESH_MEAN_C：均值类型，处理后的图像更加有棱角
cv2.ADAPTIVE_THRESH_GAUSSIAN_C：高斯类型，处理后的图像更加平滑

blockSize 好像必须是奇数，越小图像越细腻
'''
threshold = cv2.adaptiveThreshold(src=img_gray, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  thresholdType=cv2.THRESH_BINARY, blockSize=115, C=1)
cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()