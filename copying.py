import os
import cv2

folders = os.listdir('C:/Users/gyuha/Desktop/crane2crane2/testA')

directory = os.listdir('C:/Users/gyuha/Desktop/crane2crane2/testA')
os.chdir('C:/Users/gyuha/Desktop/crane2crane2/testA')
for file in directory:
    img = cv2.imread(file)
    cv2.imwrite('C:/Users/gyuha/Desktop/crane2crane2/testA/%s.jpg'%file[:-4], img)