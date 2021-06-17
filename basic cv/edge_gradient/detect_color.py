import cv2
import matplotlib.pyplot as plt
import numpy as np   


img = cv2.imread('C:\\Users\\Admin\\Desktop\\tree.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


small_pic = img[450:501, 250:351]
img_flatten = []

for i in range(3):
    a = small_pic[:,:,i].flatten()
    img_flatten.append(a)

f, (ax1, ax2, ax3,ax4) = plt.subplots(1,4, figsize=(10,5))
ax1.set_title("R")
ax1.hist(img_flatten[0])
ax2.set_title("G")
ax2.hist(img_flatten[1])
ax3.set_title("B")
ax3.hist(img_flatten[2])

def restrict(color_component):
    return np.clip(color_component, 0, 255)

alpha = 2.5
low= []
high = []

for i in range(3):
    img_flatten[i] = np.array(img_flatten[i])
    mu = img_flatten[i].mean()
    sigma = img_flatten[i].std()
    print('mu',mu)
    print('si',sigma)
    deviation = alpha*sigma
    print ('deviation',deviation)
    print ("____________")
    low.append(restrict(mu-deviation))
    high.append(restrict(mu+deviation))

print(low)
print(high)
    #print(mu)
mask_lower = np.array([low[0], low[1], low[2]])
mask_higher = np.array([high[0], high[1], high[2]])

hand_mask = cv2.inRange(img, mask_lower, mask_higher)


masked_hand = np.copy(img)
masked_hand[hand_mask != 0] = [0, 0, 0]

ax4 = plt.imshow(masked_hand)

# plt.show()

#plt.imshow(small_pic)
plt.show()

