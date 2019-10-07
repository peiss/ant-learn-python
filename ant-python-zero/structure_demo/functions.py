"""
这里可以放置这个模块module的注释
"""


class MyClass():
    """
    类注释，这是一个类
    """

    def __init__(self):
        self.name = "xiaoming"

    def get_name(self):
        return self.name

    def set_name(self, name):
        """
        设置这个类的name的值
        :param name:
        :return:
        """
        if name is not None:
            self.name = name


def max(a, b):
    """
    函数，获取a和b中大的那个值
    :param a:
    :param b:
    :return:
    """
    if a > b:
        return a
    else:
        return b


# 随意的代码块
myClass = MyClass()
myClass.set_name("xiaowang")
print(myClass.get_name())

# 调用函数
print("3 and 5 bigger is:", max(3, 5))
