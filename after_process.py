# 计算左手和右手关节点的角度
import math
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
joints = { 0 , " nose " },
{ 1 , " left_eye " },
{ 2 , " right_eye " },
{ 3 , " left_ear " },
{ 4 , " right_ear " },
{ 5 , " left_shoulder " },
{ 6 , " right_shoulder " },
{ 7 , " left_elbow " },
{ 8 , " right_elbow " },
{ 9 , " left_wrist " },
{ 10 , " right_wrist " },
{ 11 , " left_hip " },
{ 12 , " right_hip " },
{ 13 , " left_knee " },
{ 14 , " right_knee " },
{ 15 , " left_ankle " },
{ 16 , " right_ankle " }



def angle_between_points(p0, p1, p2):
    # 计算角度
    a = (p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2
    b = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    c = (p2[0] - p0[0]) ** 2 + (p2[1] - p0[1]) ** 2
    if a * b == 0:
        return -1.0

    return math.acos((a + b - c) / math.sqrt(4 * a * b)) * 180 / math.pi


def length_between_points(p0, p1):
    # 2点之间的距离
    return math.hypot(p1[0] - p0[0], p1[1] - p0[1])


def get_angle_point(ktp_point, score_pt, pos):
    # 返回各个部位的关键点
    pnts = []

    if pos == 'left_elbow':
        pos_list = (5, 7, 9)
    elif pos == 'right_elbow':
        pos_list = (6, 8, 10)
    else:
        print('Unknown  [%s]', pos)
        return pnts
    for i in range(3):
        if score_pt[pos_list[i]] <= 0.1:
            print('component [%d] incomplete' % (pos_list[i]))
            return pnts
        else:
            pnts.append((int(ktp_point[pos_list[i]][0]), int(ktp_point[pos_list[i]][1])))
    return pnts



def angle_left_elbow(human, score_pt):
    pnts = get_angle_point(human, score_pt, 'left_elbow')
    if len(pnts) != 3:
        print('component incomplete')
        return 0

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
        print('left elbow angle:%f' % (angle))
    return angle


def angle_right_elbow(human, score_pt):
    pnts = get_angle_point(human, score_pt, 'right_elbow')
    if len(pnts) != 3:
        print('component incomplete')
        return 0

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
        print('right elbow angle:%f' % (angle))
    return angle


def cv2AddChineseText(img, text, position, textColor=(255, 0, 0), textSize=60):
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "/home/hik/zhangyuxin19/edgeai-yolov5-yolo-pose/STSONG.TTF", textSize, encoding="utf-8")
    # 绘制文本
    draw.text(position, text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)





