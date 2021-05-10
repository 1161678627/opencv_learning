import cv2
import numpy as np

# 实例化一个摄像头对象，0表示第一个，1表示第二个
cap = cv2.VideoCapture(0)

'''
#详解cv2.VideoWriter_fourcc对象(摘自Learning OpenCV3 Computer Vision with Python,坦白讲不太懂)
#fourcc意为四字符代码（Four-Character Codes），顾名思义，该编码由四个字符组成,下面是VideoWriter_fourcc对象一些常用的参数，注意：字符顺序不能弄混
#cv2.VideoWriter_fourcc('I', '4', '2', '0'),该参数是YUV编码类型，文件名后缀为.avi
#cv2.VideoWriter_fourcc('P', 'I', 'M', 'I'),该参数是MPEG-1编码类型，文件名后缀为.avi
#cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'),该参数是MPEG-4编码类型，文件名后缀为.avi
#cv2.VideoWriter_fourcc('T', 'H', 'E', 'O'),该参数是Ogg Vorbis,文件名后缀为.ogv
#cv2.VideoWriter_fourcc('F', 'L', 'V', '1'),该参数是Flash视频，文件名后缀为.flv
'''
# 使用cv2写入视频到本地时，需要指定一个编码器fourcc,使用 拆包方式 快速传入参数
fourcc = cv2.VideoWriter_fourcc(*'XVID')

frame_width = int(cap.get(3))   # 获取图片帧宽度
frame_height = int(cap.get(4))  # 获取图像帧高度
print('摄像头的宽高为：', frame_width, frame_height)

# 创建一个写入视频的io流，参数依次为 指定保存视频名称，指定视频编码器，视频帧率(每秒刷新多少图像帧，越大越快)，图像帧尺寸
out = cv2.VideoWriter('my_capture_video.avi', fourcc, 30, (frame_width, frame_height))

# 如果摄像头没有打开，则退出程序
if cap.isOpened() is False:
    print('error')
    exit(1)
# 否则
else:
    while True:
        # 只有调用read方法的时候才真正启用了摄像头
        # ret表示 该帧图像 是否读取成功，返回值为True/Fales，常用于读取video时判断是否到了最后一帧
        ret, frame = cap.read()
        # print('摄像头的分辨率为：', frame.shape) (480, 640, 3)
        # 彩色图片转灰度
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 对图片进行翻转， 1 ->水平翻转，0 ->垂直翻转，-1 ->水平垂直翻转
        flip_img = cv2.flip(gray_img, flipCode=1)
        # 将处理前的图片按帧写入 视频流 中,注意视频流中不能写入 灰度图片---否则无法播放
        out.write(frame)
        # 等待1ms的键盘输入，实际效果是延时画面1帧，越小画面越流畅
        cv2.imshow(winname='mycapture', mat=flip_img)
        key = cv2.waitKey(1)
        # ord用于返回某个字符对应的ascii码，即cv2中对键盘的编码是用的ascii码，区分大小写的
        # esc对应键码为27，如果输入esc则退出循环，不再调用摄像头
        if key & 0xFF == 27:
            break

# 在程序末尾销毁所有对象
cap.release()
out.release()
cv2.destroyAllWindows()