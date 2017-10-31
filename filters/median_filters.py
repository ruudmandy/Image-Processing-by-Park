#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:50:28 2017

@author: apple
"""

import numpy as np
import matplotlib.pyplot as plt


def neighbour(pic_array,r,c):
    four_connected=[]
    """
    | x  N1  x  |  ---> (r-1,c) , (r,c-1) , (r,c+1) , (r+1,c)
    | N2 n   N3 |
    | x  N4  x  |
    """
    pos=((r-1,c),(r,c-1),(r,c+1),(r+1,c))
    
    if pos[0][0]<0 or pos[0][1]<0 or pos[0][0]>=pic_array.shape[0] or pos[0][1]>=pic_array.shape[1]:pass
    else:four_connected.append(pic_array[r-1,c])
    if pos[1][0]<0 or pos[1][1]<0 or pos[1][0]>=pic_array.shape[0] or pos[1][1]>=pic_array.shape[1]:pass
    else:four_connected.append(pic_array[r,c-1])
    if pos[2][0]<0 or pos[2][1]<0 or pos[2][0]>=pic_array.shape[0] or pos[2][1]>=pic_array.shape[1]:pass
    else:four_connected.append(pic_array[r,c+1])
    if pos[3][0]<0 or pos[3][1]<0 or pos[3][0]>=pic_array.shape[0] or pos[3][1]>=pic_array.shape[1]:pass
    else:four_connected.append(pic_array[r+1,c])
    return four_connected
      
def diagonal(pic_array,r,c):
    diagonal_connected=[]
    """
    | D1 x  D2 } ---> (r-1,c-1) , (r-1,c+1) , (r+1,c-1) , (r+1,c+1)
    | x  n  x  }
    | D3 x  D4 |
    """
    pos=((r-1,c-1),(r-1,c+1),(r+1,c-1),(r+1,c+1))
    
    if pos[0][0]<0 or pos[0][1]<0 or pos[0][0]>=pic_array.shape[0] or pos[0][1]>=pic_array.shape[1]:pass
    else:diagonal_connected.append(pic_array[r-1,c-1])
    if pos[1][0]<0 or pos[1][1]<0 or pos[1][0]>=pic_array.shape[0] or pos[1][1]>=pic_array.shape[1]:pass
    else:diagonal_connected.append(pic_array[r-1,c+1])
    if pos[2][0]<0 or pos[2][1]<0 or pos[2][0]>=pic_array.shape[0] or pos[2][1]>=pic_array.shape[1]:pass
    else:diagonal_connected.append(pic_array[r+1,c-1])
    if pos[3][0]<0 or pos[3][1]<0 or pos[3][0]>=pic_array.shape[0] or pos[3][1]>=pic_array.shape[1]:pass
    else:diagonal_connected.append(pic_array[r+1,c+1])
        
    return diagonal_connected


def all_neighbour(pic_array,r,c):
    # neighbour union diagonal. 
    all_neighbour=neighbour(pic_array,r,c)+diagonal(pic_array,r,c)+[pic_array[r,c]]
    return all_neighbour

def median(arr):
    len_arr=arr.size
    return arr[len_arr//2]


img=[plt.imread("hip_02.jpg"),plt.imread("hip-salt.jpg"),plt.imread("hip-pepper.jpg")]
new_img=[np.zeros_like(img[0]),np.zeros_like(img[1]),np.zeros_like(img[2])]
#row,col,dim=img.shape

for n_pic in range(len(new_img)):
    row,col,dim=img[n_pic].shape
    for d in range(dim):
        for r in range(row):
            for c in range(col):
                neighbour_list=np.array(all_neighbour(img[n_pic][:,:,d],r,c))
                new_img[n_pic][r,c]=median(neighbour_list)

plt.subplot(321)
plt.title('noise')
plt.imshow(img[0],cmap='gray') 
plt.subplot(322)
plt.title('Median filters')
plt.imshow(new_img[0],cmap='gray')  
plt.subplot(323)
#plt.title('salt')
plt.imshow(img[1],cmap='gray')  
plt.subplot(324)
#plt.title('Harmonic mean')
plt.imshow(new_img[1],cmap='gray')  
plt.subplot(325)
#plt.title('pepper')
plt.imshow(img[2],cmap='gray')  
plt.subplot(326)
#plt.title('Harmonic mean')
plt.imshow(new_img[2],cmap='gray')

plt.show()



        

