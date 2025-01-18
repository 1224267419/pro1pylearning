# 实操,实现文件备份
name = input("请输入要备份的文件名")
try:
    file = open(name, "r")  # 读旧文件
    # file_copy=open(name+"[复制]", "w+")#这里文字加在了.txt后
    index = name.rfind('.')  # 查找关键字,返回下标
    new_name = name[:index] + "[复制]" + name[index:]
    file_copy = open(new_name, 'w')
    lines = file.readlines()

    for line in lines:
        file_copy.write(line)
    file_copy.close()
    file.close()

except FileNotFoundError:  # 读取失败的处理
    print("不存在文件%s" % name)
