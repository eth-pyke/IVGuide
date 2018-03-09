# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Sat Feb 17 22:10:59 2018)---
runfile('C:/Users/user/.spyder-py3/temp.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
import cv2
import numpy as np

img = cv2.imread('eugeneVein.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imwrite('houghlines5.jpg',img)
debugfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
import cv2
import numpy as np

img = cv2.imread('eugeneVein.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imwrite('houghlines5.jpg',img)
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
import cv2
import numpy as np

img = cv2.imread('eugeneVein.JPG')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray,100,200,apertureSize = 3)
cv2.imshow('edges',edges)
cv2.waitKey(0)

minLineLength = 30
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow('hough',img)
cv2.waitKey(0)
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
debugfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')

## ---(Sat Feb 17 22:35:25 2018)---
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')

## ---(Sat Feb 17 22:40:09 2018)---
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
%clear
%clear
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
debugfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
debugfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/lines.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/lines.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/lines.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/lines.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/lines.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/lines.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/idk.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/dilation.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/veinDetectionA1.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/histogramEqualization.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/histogramEqualization.py', wdir='C:/Users/user/.spyder-py3')

## ---(Wed Feb 28 18:53:43 2018)---
runfile('C:/Users/user/.spyder-py3/stereoTest1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/stereoTest1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/stereoTest1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/stereoTest1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/stereoTest1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/stereoTest1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/stereoTest1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/stereoTest1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/stereoTest1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/stereoTest1.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/EdgeDetector.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/uncanny.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/uncanny.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/uncanny.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/uncanny.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/uncanny.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/uncanny.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/uncanny.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/uncanny.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/uncanny.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/uncanny.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/uncanny.py', wdir='C:/Users/user/.spyder-py3')
import cv2
import opencv
%clear
runfile('C:/Users/user/.spyder-py3/uncanny.py', wdir='C:/Users/user/.spyder-py3')
%clear
runfile('C:/Users/user/.spyder-py3/stereoTest1.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/histogramEqualization.py', wdir='C:/Users/user/.spyder-py3')