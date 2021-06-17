import cv2
import numpy as np

#buoc 1: capture video frame
vid = cv2.VideoCapture('0s_to_8s_Fire_Inferno_Stock_Footage___Royalty_.mp4')
frame_array = []
frame_width = 367
frame_height = 550
#out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

if (vid.isOpened() == False):
    print ('error')
while (vid.isOpened() == True):
    ret, frame = vid.read()
    if (ret == True):
        frame = cv2.resize(frame, (367,550))
        frame_array.append(frame)
        #out.write(frame)
        #cv2_imshow (frame)
        print (frame.shape)
        if (cv2.waitKey(15) &  0xFF == ord('q')):
            break
    else:
        break
vid.release()
#out.release()

#buoc 2: blend ảnh với từng frame 
def blend(mask, frame, girl):
    im = girl * 0.35 + frame * 0.65
    im = im.astype('float32') / 255
    mask = mask.astype ('float32') /255

    masked = im *mask
    masked = (masked * 255).astype ('uint8')
    test = girl.copy()
    for i in range (test.shape[0]):
        for j in range (test.shape[1]):
            if (np.sum(masked[i,j,:],axis = -1) == 0):
                masked[i,j,:] += test[i,j,:]
    return masked
"""mask = cv2.imread ('mask.png')
girl = cv2.imread ('girl.jpg')
result = blend (mask, frame_array[5], girl)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroywindow()"""
final = []
for frame in frame_array:
    mask = cv2.imread ('mask.png')
    girl = cv2.imread ('girl.jpg')
    result = blend (mask, frame, girl)
    final.append (result)
    #cv2.imshow(result)
#buoc 3: tạo video 
height, width, layers = final[0].shape
size = (width, height)
out = cv2.VideoWriter('project3.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 20, size)
for im in final:
    out.write(im)
out.release()
