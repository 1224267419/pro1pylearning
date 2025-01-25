# 要求每次烤地瓜时间叠加,存储用户添加的调料
def is_file_empty(file_path):
    with open(file_path, 'r') as file:
        return file.read() == ''


class Digua:
    def __init__(self, name, time, tiaoliao):
        # files_name为文件存储路径
        self.file_name = name + ".txt"  # 用于记录调料存储
        self.time = time  # 初始烤地瓜的时间
        self.counter = 0  # 统计调料数目
        a = open(self.file_name, "w")  # 初始化时创建并清空文件
        a.close()

        self.fangtiaoliao(tiaoliao)

    def kao(self, time):
        self.time = self.time + time  # 烤地瓜时间累加

    def zhuangtai(self):  # 根据被烤的时间查询对应的地瓜状态
        if (self.time < 0):
            print("错误数据")
            return "错误地瓜"
        if (self.time >= 0 and self.time < 3):
            return "生的"
        if (self.time >= 3 and self.time < 5):
            return "半生不熟"
        if (self.time >= 5 and self.time < 8):
            return "熟了"
        if (self.time >= 8):
            return "糊了"

    def fangtiaoliao(self, tiaoliao):
        if (is_file_empty(self.file_name)):  # 文件为空
            with open(self.file_name, encoding="utf-8", mode="a") as file:  # mode为a表示内容追加
                file.write(tiaoliao)
                self.counter += 1
                file.close()
        else:
            with open(self.file_name, encoding="utf-8", mode="a") as file:  # mode为a表示内容追加
                file.write ("和" + tiaoliao)
                self.counter += 1
                file.close()

    def __str__(self):
        with open(self.file_name, encoding="utf-8", mode="r") as file:
            tiaoliao = ""
            for line in file.readlines():
                tiaoliao = tiaoliao + line
            file.close()
            # return "这是一个" + self.zhuangtai() + "的加了" + tiaoliao + "的地瓜"
            return f"这个地瓜烤了{self.time}分钟,状态是{self.zhuangtai()},加了{tiaoliao}共计{self.counter}种调料"


gua1 = Digua("gua1", 3, "sugar")
gua1.kao(3)  # 额外再考
gua1.fangtiaoliao("盐")
print(gua1)
