import cv2
import numpy as np
import os
import ast
import shutil
from PIL import Image, ImageFilter
import cv2
import numpy as np
PATH = os.path.dirname(os.path.realpath(__file__))
# print(PATH)
# try:
    # f = open(PATH+'/cric_confi.txt','r')
# except:
    # f = open(PATH+'/cric_confi.txt','r')

# source = ('/Users/apple/Desktop/Backup/CricketMatch/MicrosoftTeams-image (33).png')



def segment(path):
    # imi = cv2.imread(path)
    # cv2.imshow('segmentor',imi)
    f = open(PATH + '/cric_confi.txt', 'r')
    for row in f:
        try:
            print('#######################################################',row)
            print(row)
            dict = ast.literal_eval(row)
            location = dict["location"]
            #masking_set.add(site)
            coordinates = dict["coordinates"]
            image= cv2.imread(path)
            height, width= image.shape[:2]
            ROI= np.array([coordinates], dtype= np.int32)
            blank= np.zeros_like(image)
            region_of_interest= cv2.fillPoly(blank, ROI, (255,255,255))
            region_of_interest_image= cv2.bitwise_and(image, region_of_interest)

            # if location == 10 :
            #     cv2.imwrite(PATH+'/sourceimages/'+ 91 + '.jpg', region_of_interest_image)
            #
            # else :
            #cv2.imshow('roi',region_of_interest_image)
            cv2.imwrite(PATH + '/sourceimages/' + location + '.jpg', region_of_interest_image)


        except:
            print('exception occurred')
    f.close()
