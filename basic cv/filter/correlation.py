#import cv2
import numpy as np 

"""
#doc anh va chuyen anh sang gray de giam so chieu rgb
img = cv2.imread('')
img = cv2.resize (img, (200,200))
img = cv2.cvtColor(img, cv2.COLOR_BRG2GRAY)
"""

# array tuong trung 
img = np.array([[1,2,3,2,3], [4,5,6,7,5], [7,8,9,2,5], [2,3,4,8,9], [4,5,6,1,4]])
img_height = img.shape[0]

img_width = img.shape[1]

kernel = np.array([[1,0,0], [1,0,0], [1,0,0]])/5
ker_height = kernel.shape[0]
ker_width = kernel.shape[1]

# tao lop 0 bao ben ngoai img 
result = np.zeros ((img_height + 2, img_width + 2))
result [1:-1, 1:-1] = img

# ket qua cuoi cung 
correlation = np.zeros((img.shape[0], img.shape[1]))


for i in range (img_height - (ker_height -3)):
    for j in range (img_width - (ker_height -3)):
        correlation[i,j] = (kernel * result[i:i+ker_height, j:j+ker_width]).sum()
print (correlation)
print (correlation.shape)
