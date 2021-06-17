import cv2
import numpy as np
# Buoc 1: doc anh
img = cv2.imread('./pietro-de-grandi-T7K4aEPoGGk-unsplash.jpg', 0)
img = cv2.resize(img, (400,400))
def ComputeImageGradient(img):
    # Buoc 2: tinh dao ham theo truc x
    dx = img[:,1:].astype(np.float) - img[:,:-1].astype(np.float)
    # Buoc 3: tinh dao ham theo truc y
    dy = img[1:,:].astype(np.float) - img[:-1,:].astype(np.float)
    # Buoc 4: tinh image gradient
    G = np.sqrt(dx[:-1,:]**2 + dy[:,:-1]**2)
    return G

# BUOC 6: seam carving
D = 20
G = ComputeImageGradient(img)

G = G.astype(np.uint8)
print(G[:10,:10])


# Buoc 5: hien thi anh de kiem tra xe doc dung ko
# Hien thi anh gradient
cv2.imshow('Anh goc', img)
cv2.imshow('Anh Gradient', G)
cv2.waitKey(0)
cv2.destroyAllWindows()