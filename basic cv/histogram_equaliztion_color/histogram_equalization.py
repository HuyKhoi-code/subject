import cv2
import numpy as np
#buoc 1: doc anh 
img = cv2.imread ('1_IqNKPg7wUktQDDTbk80H3Q.jpeg')
cv2.imshow ('anh goc: ',img)

# buoc 2: chuyen anh ve kenh mau HSV
img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# buoc 3: Tinh anh histogram cho kenh V
img_V = img_cvt[:,:,2]
img_vec = img_V.reshape(-1)
def cal_hist(img_vec):
    hist = np.zeros(256, np.int)
    values, counts = np.unique(img_vec, return_counts=True)
    for i, val in enumerate(values):
        hist[val] = counts[i]
    return hist
hist = cal_hist(img_vec)

# Buoc 4: Tinh CDF
cdf = np.cumsum(hist)

# Buoc 5: Tinh h(v)
cdf_min = np.min(cdf)
h = (cdf - cdf_min) / (cdf[-1] - cdf_min) * 255
h = h.astype(np.int)

# Buoc 6: can ban anh bien gia tri mau v --> h(v)
img_eq = img_V.copy()
for v in range(256):
    img_eq[img_V==v] = h[v]
img_cvt[:,:,2] = img_eq
result = cv2.cvtColor(img_cvt, cv2.COLOR_HSV2BGR)

#buoc 7: show hang
cv2.imshow ('anh da can bang', result)
#cv2.imwrite ('result.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()