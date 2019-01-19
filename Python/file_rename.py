#-*- codong:utf-8 -*-
import os
def rename():
    path="D:\\chushi\\train" #文件路径
    filelist = os.listdir(path) #该文件夹下的所有文件
    count =0

    for file in filelist: #遍历所有文件 包括文件夹
        Olddir = os.path.join(path,file)#原来文件夹的路径
        if os.path.isdir(Olddir):#如果是文件夹，则跳过
            continue
        filename = os.path.splitext(file)[0]  #文件名
        filetype = ".jpg"#os.path.splitext(file)[1]   文件扩展名
        Newdir = os.path.join(path,"cook_"+str(count)+filetype) #新的文件路径
        os.rename(Olddir,Newdir) #重命名
        count += 1
if __name__ == '__main__':
    rename()