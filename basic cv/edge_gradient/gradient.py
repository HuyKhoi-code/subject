import cv2
import numpy as np
import matplotlib.pyplot as plt



def gradient(img):
    #mask = np.zeros((img.shape[0]+1, img.shape[1] +1))
    #mask[:-1,1:] = img
    dx = img[1:,:].astype(np.float) - img[:-1,:].astype(np.float)

    dy = img[:,1:].astype(np.float) - img[:,:-1].astype(np.float)

    mask1 = np.zeros(img.shape)
    mask2 = np.zeros(img.shape)
    
    mask1[:-1,:] = dx
    mask2[:,:-1] = dy

    g= np.sqrt(mask1*mask1 + mask2*mask2)

    return g.astype(np.uint8)

img = cv2.imread('./pietro-de-grandi-T7K4aEPoGGk-unsplash.jpg',0)
img = cv2.resize(img, (400,400))
# mask = np.zeros((img.shape[0]+1, img.shape[1] +1))
# mask[:-1,1:] = img
g = gradient(img)
cv2.imshow('hello', g)
cv2.imshow('hello1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()