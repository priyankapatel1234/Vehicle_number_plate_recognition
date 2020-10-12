import numpy as np
import cv2      #install pip install opencv-python in anaconda prompt
import os
import pytesseract
import matplotlib.pyplot as plt
%matplotlib inline
#print(cv2.__version__)
#import pandas as pd

print(cv2.__version__)

def plot_images(img1,img2,title1="",title2=""):
    fig =plt.figure(figsize=[18,18])
    ax1 =fig.add_subplot(121)
    ax1.imshow(img1,cmap="gray")
    ax1.set(xticks=[],yticks=[],title=title1)
    
    ax2 =fig.add_subplot(122)
    ax2.imshow(img2,cmap="gray")
    ax2.set(xticks=[],yticks=[],title=title2)
    
    path ="./images/car.png"
    
    image= cv2.imread(path)
    
    plot_images(image,image)
    
