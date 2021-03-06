# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Axddw1xnRh-TnFpNue8MyB2ODn5X4_b6
"""
# su dung file nay trong google colab
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img = cv2.imread ('/content/pietro-de-grandi-T7K4aEPoGGk-unsplash.jpg', 0)
img = cv2.resize (img, (600,400))
# Tinh gradient de lay edge 
def ComputeImageGradient(img):
    # Buoc 2: tinh dao ham theo truc x
    dx = img[:,1:].astype(np.float) - img[:,:-1].astype(np.float)
    # Buoc 3: tinh dao ham theo truc y
    dy = img[1:,:].astype(np.float) - img[:-1,:].astype(np.float)
    # Buoc 4: tinh image gradient
    G = np.sqrt(dx[:-1,:]**2 + dy[:,:-1]**2)
    return G

G = ComputeImageGradient(img)
cv2_imshow (img)
print ("---")
cv2_imshow (G)

# tinh cost cua tung pixel va duong di co cost be nhat
def Cost_map (img):
    # tao ma tran mask co nhieu hon img 1 cot va 1 hang 
    # sau khi tinh gradient cua mask, img va G se co cung kich thuoc
    img_mask = np.zeros((img.shape[0]+1, img.shape[1]+1))
    img_mask [1:,:-1] = img

    # tinh gradient cua anh 
    Gradient = ComputeImageGradient(img_mask)
    Gradient = Gradient.astype(np.uint8)
    
    r, c = Gradient.shape

    cost_matrix = Gradient.copy()
    track_matrix = np.zeros (cost_matrix.shape,dtype=np.int)
    # tai moi pixel, tinh cost nho nhat cho toi no va luu lai vi tri cua pixel noi voi no 
    # xet trong 3 pixel tu j-1 : j+2
    for i in range (1,r):
        for j in range (0,c):
            if j == 0 :
                # tim vi tri cua pixel nho nhat (vi tri so voi j)
                min_index = np.argmin(cost_matrix[i-1, j : j+2])
                # gan vi tri cua pixel nho nhat cua row i-1 tren vao tracking matrix [i,j]
                track_matrix[i, j] = min_index + j 
                # gia tri cua pixel nho nhat
                min_cost = cost_matrix[i-1, min_index+j]
            else:
                min_index = np.argmin(cost_matrix[i-1, j-1 : j+2])
                track_matrix[i, j] = min_index + j - 1
                min_cost = cost_matrix[i-1, min_index + j - 1]
        # tinh trong so nho nhat tai tung pixel 
            cost_matrix[i,j] += min_cost

    return cost_matrix, track_matrix

def seam_carving (img):
    r, c = img.shape
    cost, track = Cost_map(img)

    # tao mang phu g???m c??c ph???n t??? True    
    mask = np.ones((r, c), dtype=np.bool)

    # xet phan tu co gia tri nho nhat o hang cuoi cung
    j = np.argmin(cost[-1])

    # truy vet duong seam nguoc len
    for i in reversed(range(r)):
        #danh dau vi tri cua cac phan tu trong duong seam
        mask[i, j] = False
        j = track[i, j]

    # loai bo duong seam ra khoi ma tran
    img = img[mask].reshape((r, c - 1))

    return img

img2 = img
for i in range (250):
    img2 = seam_carving(img2)
cv2_imshow(img2)
cv2_imshow (img)

filename = 'image after seam carving.jpg'
cv2.imwrite (filename, img2)