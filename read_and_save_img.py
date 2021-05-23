import cv2
from matplotlib import pyplot as plt
import numpy as np

# 其中flags参数可以传0-表示以灰度形式读取， 1-表示读取彩色图片
# 注意 opencv返回的图片array通道排列是 BGR
img = cv2.imread(filename='./watch.jpg', flags=1)

# 打印读取的像素信息, ndarray
print('图片的类型是：', type(img))

# 打印图片shape信息
img_height, img_width, img_deep = img.shape
print('图片的高、宽、深度是：', img_height, img_width, img_deep)

# 打印图片像素的数目, = 高*宽*深
img_size = img.size
print('图片全部的像素数是：', img_size)

# 展示图片，窗口title为必要参数
# 这个窗口会随着主程序进程的结束而自动销毁，不像plt那种会一直在绘画面板中，若要持续显示，需要配合cv2.waitKey使用，不能用time.sleep代替waitKey
cv2.imshow('mywatch', img)

# 写入一个像素数组为img到本地
cv2.imwrite('./write_gray_watch.jpg', cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

# delay 参数控制等待键盘输入多少ms，当输入参数为0或者None时，表示持续等待键盘输入一个 按键
# 当在delay时间内，捕获键盘输入，则该句执行结束，否则等到 等待时间到达后，该句结束
# 其返回值为 键盘输入的键码
cv2.waitKey(delay=0)

# 一般放在程序的最后，销毁所有cv2窗口
cv2.destroyAllWindows()

# 在展示原图和处理后的对比图时，除了imshow两次外，可以考虑另一种方式，用np将两个图 水平、垂直 拼接成一张图展示出来 hstack 水平，vstack垂直
img3 = np.hstack((img, img))
cv2.imshow('hstack', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()