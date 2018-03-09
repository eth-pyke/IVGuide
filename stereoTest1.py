# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:53:55 2018

@author: user
"""

import numpy as np
import cv2 
import matplotlib.pyplot as plt
     
imgL = cv2.imread('stereoVeinL.jpg',0)
imgR = cv2.imread('stereoVeinR.jpg',0)
     
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()