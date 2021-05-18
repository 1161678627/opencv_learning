import cv2
import numpy as np

# 首先从 http://tools.jb51.net/static/colorpicker/ 网站中得到我们要筛选区间的颜色 rgb值
# 或者使用截图工具，选中当前颜色的rgb值，然后在这里转换为hsv的upper和lower
# 然后使用如下代码将 rgb转为cv2中 hsv色系的 lower_ upper_值，用于后续在inrange中筛选颜色
rgb_value = np.uint8([[[160, 89, 35]]])
hsv_value = cv2.cvtColor(rgb_value, cv2.COLOR_RGB2HSV)
print(hsv_value)

cap = cv2.VideoCapture(0)
while True:
    # 从摄像头读取一帧图片
    ret, frame = cap.read()
    if not ret:
        print('摄像头故障，程序退出')
        break
    # 然后将该图像从rgb空间转换到hsv空间，这有利于我们对他进行颜色过滤
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 注意upper的每一个值都要比 lower大才行，否则 show黑屏
    # 当然这里的颜色区域，也可以从hsv对照表直接选区间确定——不过有时选取的区间会比较大，杂色会比较多，需要慢慢过滤
    lower_ = np.array([10, 180, 160])
    upper_ = np.array([25, 255, 180])
    # 该函数的用途为将低于lowerb 和 高于 upperb 的部分都变成0，在这之间的颜色都变为255,其返回一个二值的mask用于后续的颜色提取处理
    # 因为rgb体系中不好确定颜色之间的渐变，颜色之间没有大中小的范围过滤，所以需要转换到hsv体系里面，hsv体系中每种颜色有渐变的数值，用于筛选颜色
    # 如果使用cvtColor函数，并设置参数为CV_BGR2HSV,那么所得的H、S、V值范围分别是[0,180)，[0,255)，[0,255)，而非[0,360]，[0,1]，[0,1]
    # 此时由于传入的src是hsv色系的，所以给出的lower 和 upper也需要符合hsv色系才行
    # 返回的mask即目标区域是白色，其他都是黑色
    mask = cv2.inRange(src=hsv, lowerb=lower_, upperb=upper_)
    # print(mask.shape)
    # 使用bitwise_and操作，将mask掩码中白色的部分，其实就是筛选出来的颜色部分，进行源图图像的颜色填充
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('cap', mask)

    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()