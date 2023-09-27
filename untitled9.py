# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 12:24:59 2023

@author: arab
"""

import cv2
import numpy as np
import os
import glob
import os.path as osp


#load data
DirPath = 'F:/Arshan_Abbas/Fabian/Task2/Img'

idx = 0
Files = os.listdir(DirPath)
for File in Files:
    imgPath = os.path.join(DirPath,File)
    print(imgPath)
    idx += 1
    base = osp.splitext(osp.basename(File))[0]
    image = cv2.imread(imgPath)
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 50, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # counting the number of pixels
    number_of_green_pix = np.sum(image[:,:,1] == 255, where=((image[:,:,0] == 0) & (image[:,:,2] == 0)))
    number_of_black_pix = np.sum(File == 0)
    draw1 = cv2.drawContours(image, contours, -1, (255, 255, 255), 1)
    draw2 = cv2.drawContours(imgray, contours, -1, (255, 255, 255), 1)
    SaveDir = 'F:/Arshan_Abbas/Fabian/Task2/Imgedit/'
    output_file_path = os.path.join(SaveDir, File)
    cv2.imwrite('F:/Arshan_Abbas/Fabian/Task2/Imgedit/{:s}_1pxNormal.jpg'.format(base), draw1)
    
cv2.destroyAllWindows()