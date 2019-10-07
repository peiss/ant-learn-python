class Sgrade:
    """
    学生成绩
    """

    def __init__(self, sno, yuwen, shuxue, yingyu):
        """
        初始化方法
        :param sno: 学号
        :param yuwen: 语文成绩
        :param shuxue: 数学成绩
        :param yingyu: 英语成绩
        """
        self.sno = sno
        self.yuwen = int(yuwen)
        self.shuxue = int(shuxue)
        self.yingyu = int(yingyu)


class SgradeTable:
    """
    学生成绩表
    """

    def __init__(self):
        self.sgrade_table = []


    def load_data(self, fname_sgrade_table):
        """
        载入成绩表文件
        :param fname_sgrade_table: 成绩表文件名
        :return:
        """
        with open("input.txt") as fin:
            for line in fin:
                line = line.strip()
                sno, yuwen, shuxue, yingyu = line.split("\t")
                sgrade = Sgrade(sno, yuwen, shuxue, yingyu)
                self.sgrade_table.append(sgrade)

        print("sgrade table size:", len(self.sgrade_table))


    def compute_avg_score(self):
        """
        计算各科的平均分
        :return:
        """
        yuwen_total, shuxue_total, yingyu_total = 0,0,0

        for sgrade in self.sgrade_table:
            yuwen_total += sgrade.yuwen
            shuxue_total += sgrade.shuxue
            yingyu_total += sgrade.yingyu

        count = len(self.sgrade_table)
        return yuwen_total/count, shuxue_total/count, yingyu_total/count

    def compute_max_score(self):
        """
        计算各科的最高分
        :return:
        """
        yuwen_max, shuxue_max, yingyu_max = 0, 0, 0

        for sgrade in self.sgrade_table:
            if sgrade.yuwen>yuwen_max:
                yuwen_max = sgrade.yuwen
            if sgrade.shuxue>shuxue_max:
                shuxue_max = sgrade.shuxue
            if sgrade.yingyu>yingyu_max:
                yingyu_max = sgrade.yingyu

        return yuwen_max, shuxue_max, yingyu_max


# 创建成绩表的实例
sgrade_table = SgradeTable()

# 加载成绩表文件
sgrade_table.load_data("input.txt")

# 打印平均分和最高分
print(sgrade_table.compute_avg_score())
print(sgrade_table.compute_max_score())