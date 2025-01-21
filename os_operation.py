import os

#
# os.remove("files_os.txt")  # 删除文件
# os.rename("files_os.txt", "files_os.txt2")  # 改变文件名(也可以重命名文件夹
# os.mkdir("123")#创建文件夹,重复会报错
# os.rmdir("123")#删除文件夹（要求文件夹为空
print(os.getcwd())  # 当前目录
#
# os.chdir("D:\project")#修改当前目录（./的位置
# print(os.getcwd())

print(os.listdir("123"))#用一个list列出目标文件夹的所有文件名字