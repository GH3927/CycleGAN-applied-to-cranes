import numpy as np
import cv2
import shutil
import os
import random

folders = os.listdir('C:/Users/gyuha/OneDrive - 충남대학교/메카트로닉스 (대학원)/인공지능응용/Project/crane2')

for folder in folders:
    directory = os.listdir('C:/Users/gyuha/OneDrive - 충남대학교/메카트로닉스 (대학원)/인공지능응용/Project/crane2/%s'%folder)
    os.chdir('C:/Users/gyuha/OneDrive - 충남대학교/메카트로닉스 (대학원)/인공지능응용/Project/crane2/%s'%folder)
    for file in directory:
        img = cv2.imread(file) #image file 불러옴
        img1 = img[:,:256,:]
        img2 = img[:,256:,:]
        cv2.imwrite('C:/Users/gyuha/Desktop/crane/A/%s'%file, img1)
        cv2.imwrite('C:/Users/gyuha/Desktop/crane/B/%s'%file, img2)

print('End')