import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

#pixels of a frame = 3264 * 2448
# def frame_counter(videoCapture):
#     frame_count = 0
#     while (ret0 == True):
#         ret0, frame0 = videoCapture.read()
#         if ret0 is False:
#             break
#         frame_count = frame_count + 1
#     return frame_count
# 1200:1400  1450:1650
def Width(frame0):
    return frame0.shape[1]

def Height(frame0):
    return frame0.shape[0]

def CutFrame(f, a, b):
    _f = f[a:b]
    return _f

def Difference(videoCapture1, videoCapture2, number_frame):
    sum_dif = 0
    overall_space = []
    diff = []
    for m in range(number_frame - 1):
        print(m , end='\r')  # show running
        dif = 0
        ret1, frame1 = videoCapture1.read()  # start from frame1
        ret2, frame2 = videoCapture2.read()  # start from frame0
        f1 = np.array(frame1)
        np.squeeze(f1)
        f2 = np.array(frame2)
        np.squeeze(f2)
        CutFrame(f1, 250, 750)
        CutFrame(f2, 250, 750)
        dif += np.sum(np.abs(f1 - f2))
        sum_dif += dif
        overall_space.append(sum_dif)
        diff.append(dif)
    plt.plot(diff, c='r')
    plt.plot(overall_space, c='b')
    plt.title('Summary & Differential of pixel changes')
    plt.show()

def show_slime_occupy(VideoCapture, number_frame, num_out):
    for i in range(number_frame//num_out):
        ret, frame = VideoCapture.read()
    for i in range(0, number_frame-number_frame//num_out-1, number_frame//num_out):
        for j in range(number_frame // num_out):
            ret, frame = VideoCapture.read()
        f = frame[975:1475]
        p = 0
        for x in range(500):
            for y in range(3264):
                if f[x][y][0] <= 48:#Changed here!!!
                    f[x][y] = [0, 0, 255]
                    p += 1
        print(i+number_frame//num_out, ':', p * 100 // (200 * 3264), '%')
        cv2.imwrite('%d'%i+'622slime_occupy.jpg', f)


def Capture_Yellow(videoCapture, number_frame):
    yellow_pixel = []
    for m in range(number_frame):
        n_yellow = 0
        ret, frame = videoCapture.read()
        f = np.array(frame)
        np.squeeze(f)
        f_c = CutFrame(f, 975, 1475)
        f_b = f_c[:,:,0]
        np.squeeze(f_b)
        flag = np.ones((500, 3264))
        flag *= 48
        f_b = np.mat(f_b)
        flag = np.mat(flag)
        f_b = f_b - flag
        f_b = np.array(f_b)
        # print(f_b.shape)
        # print(f_b[499][3263])
        for i in range(500):
            for j in range(3264):
                if f_b[i][j] < 0:
                    n_yellow += 1
        print(m, n_yellow)
        yellow_pixel.append(n_yellow)
    #print(yellow_pixel)
    diff = []
    for i in range(len(yellow_pixel)-1):
        dif = yellow_pixel[i+1] - yellow_pixel[i]
        diff.append(dif)

    # diff2 = []
    # for i in range(0,number_frame,30):
    #     dif = yellow_pixel[i] - yellow_pixel[i-30]
    #     diff2.append(dif)
    #
    # plt.plot(diff2, c='g')

    plt.plot(diff, c = 'r')
    plt.plot(yellow_pixel, c = 'b')
    plt.title('Summary & Differential of yellow pixel')
    plt.xlabel('Frames')
    plt.ylabel('Number of Pixels/%')
    plt.show()


def main():
    file = '2021-06-22.mp4'
    videoCapture0 = cv2.VideoCapture(file)
    videoCapture1 = cv2.VideoCapture(file)
    videoCapture2 = cv2.VideoCapture(file)
    videoCapture3 = cv2.VideoCapture(file)
    ret0, frame0 = videoCapture1.read()
    #width = Width(frame0)
    #height = Height(frame0) # Used to determine the range of the pixels we need
    #print('The width of the frame is ', width, '.  The height of the frame is ', height)
    number_frame = 4638   #frame_counter(videoCapture0)
    Capture_Yellow(videoCapture0, number_frame)
    # #Difference(videoCapture1, videoCapture2, number_frame)
    # show_slime_occupy(videoCapture3, 3, 2)




main()


