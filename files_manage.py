# 1,打开open
# r只读,w只写,w+读写,a在末尾追加
a = open('files.txt', 'r')  # w和a方式如果文件不存在会自动创建(r不会
# a = open('files.txt', 'w+')  # w+会先覆盖原内容
# a.seek()#用于改变文件指针,其中  offest:偏移量, whence:起始位置:0开头,1当前,2结尾
# 2.i读写操作write(),read()
# a.write("123")
# print(a.readline())#默认读取第一行
# print(a.readline())#再调用一次读取下一行
# print(a.readlines())  # 按行读取,每一行作为list的一个元素
# print(a.readlines()[1])#第i+1行的元素
# print(a.read(5))  # 参数为读取的数据长度(单位为B,空则表示读取所有数据
# 3.关闭c1ose()
a.close()
