import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('C:\\Users\\Admin\\Desktop\\Untitled-9.jpg', 0)
img = cv2.resize(img, (300,300))
img = cv2.blur(img,(5,5))

#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
thresh1= cv2.Canny(img, 40, 30)
cv2.imshow("input", img)


mask = np.zeros((img.shape[0]+1,img.shape[1]+1))
mask[:-1,:-1] = thresh1
mask_hope = mask.copy()

fig = plt.figure(figsize=(10,5))
fig.add_subplot(1,2,1)  
plt.imshow(mask,cmap='gray')
plt.title('before')

def dilate(matrix):
    t = matrix.reshape(-1)
    if 255 in t:    return 255
    return 0

def erode(matrix):
    t = matrix.reshape(-1)
    if 0 in t:    return 0
    return 255


for i in range(1,len(mask[0])):
    for j in range(len(mask[1])-1):
        matrix = mask[i-1:i+3,j:j+4]
        #print(len(matrix), len(matrix[0]))
        mask_hope[i][j] = dilate(matrix)
        #mask_hope[i][j] = mask[i][j]
fig.add_subplot(1,2,2)
plt.imshow(mask_hope,cmap='gray')
plt.title('hand made')

plt.show()
