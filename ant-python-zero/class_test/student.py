
class Student:
    """
    学生类
    """

    # 类变量，学生的数目
    total_cnt = 0

    def __init__(self, name, age):
        """
        初始化方法
        :param name: 姓名
        :param age: 年龄
        """
        self.name = name
        self.age = age
        Student.total_cnt += 1

    def set_grade(self, grade):
        """
        设定学生的成绩
        :param grade:
        :return:
        """
        self.grade =  grade


    def print_info(self):
        """
        打印学生的信息
        :return:
        """
        print("sutdent info", self.name, self.age, self.grade)


# 创建两个类的实例
s1 = Student("xiaoming", 20)
s2 = Student("xiaowang", 25)

# 打印类变量
print(Student.total_cnt)

# 设定学生的成绩
s1.set_grade(100)
s2.set_grade(99)

# 调用Print的普通函数
s1.print_info()
s2.print_info()
