from __future__ import absolute_import
import cv2
from random import shuffle
import os
import time
# from model import inference
from .inference_model import inference
from .segmentor import segment


PATH = os.path.dirname(os.path.realpath(__file__))


zone = [1,2,3,4,5,6,7,8,9,10]
map={}
#key = cv2. waitKey(1)
#webcam = cv2.VideoCapture(1)

def get_metadata():
    jerseyNumbers = [27, 7, 25, 5, 4, 34, 20, 16, 18, 11]
    position = [(170,683), (601,203), (601,683), (601,1163), (1083,1001) , (1083,343), (1461,203), (1461,683),(1461,1163), (1802,683)]
    global map
    map={}
    key = cv2. waitKey(1)


    shuffle(jerseyNumbers)
    print(jerseyNumbers)
    image = cv2.imread(PATH + '/Picture1.png')
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    color = (255, 255, 255)
    thickness = 10
    image = cv2.putText(image, '', (100,40), font,fontScale, color, thickness, cv2.LINE_AA)

    for i in range(len(position)):
        org= position[i]
        image = cv2.putText(image, str(jerseyNumbers[i]), org, font,fontScale, color, thickness, cv2.LINE_AA)
        map[zone[i]]=jerseyNumbers[i]

    tmp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(image)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)
    # dst = cv2.rotate(dst,cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(PATH + "/position/positions.png",dst)
    # return "/position/positions.png"

def liveView():
    #key = cv2. waitKey(1)
    key = cv2.waitKey(1)
    webcam = cv2.VideoCapture(0)
    cv2.waitKey(3000)
    ret,frame =webcam.read()
    cv2image= cv2.cvtColor(webcam.read()[1],cv2.COLOR_BGR2RGB)
    # cv2.imshow('Live_View', frame)
    # cv2. waitKey(1)

    return webcam,frame


def cam(cap):
    ret,frame =cap.read()
    cv2.imwrite(PATH +'/resultImages/recent_picture.jpg', frame)

    # sim = cv2.imread(PATH +'/resultImages/recent_picture.jpg')

    # cv2.imshow('genimage',sim)

    return True



def process():

    # imi = cv2.imread(PATH +'/resultImages/recent_picture.jpg')
    # cv2.imshow('process', imi)

    segment(PATH +'/resultImages/recent_picture.jpg')
    # cv2.imshow('segment',PATH +'/resultImages/recent_picture.jpg')
    a = inference()

    print('This is map : ',map)
    print('This is a : ',a)
    t=10
    s=0
    inp = list(map.values())
    out = list(a.values())
    out1 = [int(i) for i in out]

    print(inp)
    #print(out)
    print(out1)
    if len(inp) == 0:
        print('Length of string is 0')
        return 0
    else:
        for i in range(len(zone)):
            #print(val,',', out[i])
            if inp[i] == out1[i]:
                s= int(s + 1)
            #print(s)
        score=((s/t)*100)
        s2=round(score, 2)
        print('You score is:', s2)
        return s2
