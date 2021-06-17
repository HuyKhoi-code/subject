import cv2
import numpy as np

#buoc 1: doc anh 
img = cv2.imread ('girl.jpg')
cv2.imshow('img',img)
fire = cv2.imread ('fire.jpg')
cv2.imshow('fire',fire)
mask = cv2.imread ('mask.png')
cv2.imshow ('mask', mask)
# buoc 2: tao mask blend voi fire
def blend(img, fire, mask, alpha):
    im = img * alpha + fire * (1-alpha)
    im = im.astype('float32')/255
    mask = mask.astype('float32')/255
    blend_mask = im * mask
    blend_mask = (blend_mask * 255).astype('uint8')
    return blend_mask
#buoc 3: ap blend mask vao image
blend_mask = blend(img, fire, mask, 0.2)
layer = img.copy()
for i in range(layer.shape[0]):
    for j in range(layer.shape[1]):
        if (np.sum(blend_mask[i,j,:], axis = -1) == 0):
            blend_mask[i,j,:]+= layer[i,j,:]
cv2.imshow('result',blend_mask)
cv2.imwrite('result.jpg', blend_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
