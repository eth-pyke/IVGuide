# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:44:28 2018

@author: user
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('eugeneVein.jpg',0)
edges = cv2.Canny(img,10,20)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()