from __future__ import print_function, division, absolute_import
import pandas as pd
import torch
import torch.backends.cudnn as cudnn
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import copy
import PIL.Image as Image
cudnn.benchmark = True
plt.ion()   # interactive mode
from PIL import Image, ImageFilter
import collections
PATH = os.path.dirname(os.path.realpath(__file__))

print(PATH)


def inference():
    model2 = torch.hub.load(PATH+"/yolo_new/yolo_new/yolov5", 'custom', path = PATH+'/best2.pt', source='local', force_reload=True)
    model2.conf = 0.6
    source = PATH +'/sourceimages'
    subdir =  PATH +'/'
    res={}
    for subdir, dirs, files in os.walk(source):
        for file in files:

            print(os.path.join(subdir,file))
            upath=os.path.join(subdir,file)
            im1 = Image.open(upath)

            # im2 = im1.filter(ImageFilter.UnsharpMask(radius = 2, percent = 300, threshold = 5))
            # img = np.array(im2)
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            #cv2.imshow('Raw Image',img)
            #print("----Entering Model2----")
            #img = cv2.imread()
            results = model2(im1)
            # results.show()
            #print("exiting MOdel2")
            a = results.xyxy[0]
            results.xyxy[0]  = a[a[:, 5] < 15]
            #print(results.xyxy[0])
            results.print()
            n = results.pandas().xyxy[0]
            print(n)
            file=str(file[:-4])
            if not n.empty:
                res[file]= n.iloc[-1]['name']
            else:
                n = 0
                res[file]= n


    print(res)
    od = collections.OrderedDict(sorted(res.items()))
    return od

