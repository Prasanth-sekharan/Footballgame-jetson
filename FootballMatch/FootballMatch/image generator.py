
# importing cv2
import cv2
from random import shuffle
import time
from model import inference

jerseyNumbers = [10, 25, 20, 41, 42, 8, 20, 7, 99]
position = [(351,201), (751,161), (1075,183), (1303,583), (761,381) , (733,765),(1125,945) , (747,973),(399,939)]
zone = [1,2,3,4,5,6,7,8,9]
map={}

#path= str('/Users/apple/Desktop/Backup/CricketMatch/IMG_20221110_174200.jpg')
print(jerseyNumbers)
print('\n')
#shuffle(jerseyNumbers)
print(jerseyNumbers)
image = cv2.imread('Picture1.png')

window_name = 'Cricket Match'
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2
color = (255, 255, 255)
thickness = 10
image = cv2.putText(image, 'Remember the Numbers and their Positions', (100,40), font,fontScale, color, thickness, cv2.LINE_AA)

for i in range(len(position)):
    org= position[i]
    image = cv2.putText(image, str(jerseyNumbers[i]), org, font,fontScale, color, thickness, cv2.LINE_AA)
    map[zone[i]]=jerseyNumbers[i]
#print(map)
cv2.imshow(window_name, image)
cv2.waitKey(0)

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

