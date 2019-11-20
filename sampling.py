import shutil
import os
import random

directory = os.listdir('C:/Users/gyuha/Desktop/dock6/image/')
directory1 = random.sample(directory, 900)
directory2 = random.sample(directory1, 100) #val
directory3 = [] #train
directory4 = [] #test
for i in directory1:
    if i not in directory2:
        directory3.append(i)
        
for i in directory:
    if i not in directory1:
        directory4.append(i)

for file in directory3:
    src = 'C:/Users/gyuha/Desktop/dock6/image/%s'%file
    dst = 'C:/Users/gyuha/Desktop/dock6/dataset/train'
    shutil.copy(src, dst)    

for file in directory2:
    src = 'C:/Users/gyuha/Desktop/dock6/image/%s'%file
    dst = 'C:/Users/gyuha/Desktop/dock6/dataset/val'
    shutil.copy(src, dst)
    
for file in directory4:
    src = 'C:/Users/gyuha/Desktop/dock6/image/%s'%file
    dst = 'C:/Users/gyuha/Desktop/dock6/dataset/test'
    shutil.copy(src, dst)
    
