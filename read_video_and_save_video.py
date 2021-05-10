import cv2

# VideoCapture传入数字时开启pc摄像头，传入str时，读入文件路径
cap = cv2.VideoCapture('./my_capture_video.avi')

# 如果视频流没有打开
if cap.isOpened() is False:
    print('error')
    exit(1)
else:
    # 返回的是一个float，需要int下
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    print('获取到当前视频的图像帧大小为：', frame_width, frame_height)
    # 创建视频写入的编码器
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # 100 这个参数越大视频越快
    out = cv2.VideoWriter('flip_video.avi', fourcc, 100, (frame_width, frame_height))

    while True:
        ret, img = cap.read()
        if ret is False:
            print('视频帧读入完毕')
            break
        else:
            flip_img = cv2.flip(img, flipCode=1)
            out.write(image=flip_img)
            cv2.imshow('flip img', flip_img)
            cv2.waitKey(30)
    out.release()

cap.release()
cv2.destroyAllWindows()