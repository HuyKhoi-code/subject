import cv2

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

imageTrain = 'box.png'
imageTest = 'box_in_scene.png'

img1 = cv.imread(imageTrain) # trainImage
img2 = cv.imread(imageTest) # test

# Detect keypoints using SIFT feature
sift = cv.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)


# Display traning image and testing image
vis_point1 = cv.drawKeypoints(img1,kp1, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
vis_point2 = cv.drawKeypoints(img2,kp2, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
fx, plots = plt.subplots(1, 2, figsize=(20,10))

plots[0].set_title("Training Image")
plots[0].imshow(vis_point1)
plots[1].set_title("Test Image")
plots[1].imshow(vis_point2)

#plt.show()

bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < 0.9*n.distance:
        good.append(m)


src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2) # danh sach toa do cac diem anh train (duoc danh gia la good)
dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2) # danh sach toa do cac diem anh test (tuong ung connect voi train)

#print (src_pts)
#print (dst_pts)
# Cai dat thuat toan RANSAC o day
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)# 
matchesMask = mask.ravel().tolist()
#print (matchesMask)
#print (M)
h,w,k = img1.shape

pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
dst = cv2.perspectiveTransform(pts,M)
print (dst)

img2 = cv2.polylines(img2,[np.int32(dst)],True,(160,30,250),3, cv2.LINE_AA)
#cv2.imshow('img2',img2)
draw_params = dict(matchColor = (0,255,100), 
                   singlePointColor = None,
                   matchesMask = matchesMask, 
                   flags = 2)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
cv2.imwrite('final.jpg', img3)
plt.figure(figsize=(9,16))
plt.imshow(img3, 'gray')
plt.show()

