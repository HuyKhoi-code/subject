# -*- coding: utf-8 -*-
"""Hough_Transform.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m_ELp-Uw0VMqCmjZervqBqYXgewhKtB1
"""

import math
import cv2
import numpy as np
def houghlines(img, rho=1, theta=np.pi/180, threshold=100):
    img_height, img_width = img.shape[:2]
    diagonal_length = int(math.sqrt(img_height*img_height + img_width*img_width))
    num_rho = int(diagonal_length / rho)
    num_theta = int(np.pi / theta)
    edge_matrix = np.zeros([2*num_rho+1, num_theta])
    idx	= np.squeeze(cv2.findNonZero(img))
    range_theta = np.arange(0, np.pi, theta)
    theta_matrix = np.stack((np.cos(np.copy(range_theta)), np.sin(np.copy(range_theta))), axis=-1)
    vote_matrix = np.dot(idx, np.transpose(theta_matrix))
    for vr in range(vote_matrix.shape[0]):
        for vc in range(vote_matrix.shape[1]):
            rho_pos = int(round(vote_matrix[vr, vc]))+num_rho
            edge_matrix[rho_pos, vc] += 1
    line_idx = np.where(edge_matrix > threshold)
    rho_values = list(line_idx[0])
    rho_values = [r-num_rho for r in rho_values]
    theta_values = list(line_idx[1])
    theta_values = [t/180.0*np.pi for t in theta_values]
    
    line_idx = list(zip(rho_values, theta_values))
    line_idx = [[li] for li in line_idx]
    return line_idx

def main():
    # read image
    img = cv2.imread('/content/g2-1499051410784.jpg')
    # convert to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # color -> gray
    ret,thresh1 = cv2.threshold(gray,220,250,cv2.THRESH_BINARY)
    edges = cv2.Canny(thresh1, 50, 150, apertureSize=3) 
    lines = houghlines(edges, rho=1, theta=np.pi/180, threshold=100)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)    
    cv2.imwrite('done.jpg',img)
if __name__ == "__main__":
    main()
    print('Done')