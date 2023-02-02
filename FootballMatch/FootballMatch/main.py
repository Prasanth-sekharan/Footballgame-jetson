
# importing cv2
import cv2
from random import shuffle
import time
from inference_model import inference
from segmentor import segment

jerseyNumbers = [10, 25, 20, 41, 42, 8, 20, 7, 99]
position = [(351,201), (751,161), (1075,183), (1303,583), (761,381) , (733,765),(1125,945) , (747,973),(399,939)]
zone = [1,2,3,4,5,6,7,8,9]
map={}
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)


def cam():
    ret,frame =webcam.read()
    cv2.imwrite('recent_picture.jpg', frame)


def liveView():
    #key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    ret,frame =webcam.read()
    cv2.imshow('Live_View', frame)
    cv2. waitKey(1)


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    #print("stop")
    return time


print(jerseyNumbers)
print('\n')
shuffle(jerseyNumbers)
print(jerseyNumbers)
image = cv2.imread('Picture1.png')


# NO need to use in UI
window_name = 'Cricket Match'
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2
color = (255, 255, 255)
thickness = 10
# image = cv2.putText(image, 'Remember the Numbers and their Positions', (100,40), font,fontScale, color, thickness, cv2.LINE_AA)
image = cv2.putText(image, '', (100,40), font,fontScale, color, thickness, cv2.LINE_AA)

#time=countdown(10)
#image = cv2.putText(image, 'Time Remaining:'+ str(time), (800,40), font,fontScale, color, thickness, cv2.LINE_AA)
t1=10
t=0
for i in range(len(position)):
    org= position[i]
    image = cv2.putText(image, str(jerseyNumbers[i]), org, font,fontScale, color, thickness, cv2.LINE_AA)
    map[zone[i]]=jerseyNumbers[i]

# while t < 10:
#     for i in range(len(position)):
#         org= position[i]
#         image = cv2.putText(image, str(jerseyNumbers[i]), org, font,fontScale, color, thickness, cv2.LINE_AA)
#         image = cv2.putText(image, 'Time Remaining:'+ str(t1), (100,1100), font,fontScale, color, thickness, cv2.LINE_AA)
#         map[zone[i]]=jerseyNumbers[i]
#     t = t + 1
#     t1 = t1 - 1
#     cv2.imshow(window_name, image)
#     cv2.waitKey()
#     time.sleep(1)
#print(map)
liveView()
cam()
segment('recent_picture.jpg')

a = inference()
print(map)
print(a)
t=9
s=0
inp = list(map.values())
out = list(a.values())
out1 = [int(i) for i in out]

print(inp)
#print(out)
print(out1)
for i in range(len(zone)):
    #print(val,',', out[i])
    if inp[i] == out1[i]:
        s= int(s + 1)
    #print(s)
score=((s/t)*100)
print('You score is:', score)

