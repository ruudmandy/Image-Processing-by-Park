#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image=misc.imread("lena.png")
width_col,height_col,dim_col = image.shape

#Dot operation like stackoverflow or wiki said
image_gray1 = np.dot(image[...,:3],[0.299, 0.587, 0.114])
image_gray2 = np.dot(image[...,:3],[0.333, 0.333, 0.333])
image_gray3 = np.dot(image[...,:3],[0.21, 0.71, 0.07])
width_gray,height_gray = image_gray.shape
'''R_image=image*np.array([1,0,0],dtype='uint8')
G_image=image*np.array([0,1,0],dtype='uint8')
B_image=image*np.array([0,0,1],dtype='uint8')
'''
plt.subplot(221)
plt.title("Original Image")
plt.imshow(image)
'''plt.subplot(334)
plt.imshow(R_image)
plt.subplot(335)
plt.imshow(G_image)
plt.subplot(336)
plt.imshow(B_image)'''
plt.subplot(222)
plt.title("Gray Scale Image")
plt.imshow(image_gray,cmap='gray')

plt.subplot(223)
plt.title("Gray Scale Image(average)")
plt.imshow(image_gray2,cmap='gray')

plt.subplot(224)
plt.title("Gray Scale Image(Luminous)")
plt.imshow(image_gray3,cmap='gray')