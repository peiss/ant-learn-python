"""
使用随机的方法，生成一个日志文件，用于统计程序的测试
文件输出：blog_access.log
文件字段：[到访时间、用户ID、页面ID、事件]，即"某个时间的某个人在某个地方坐了某个事"

注释：其中事件分为show/click代表页面的展示或者按钮点击
"""
import datetime
import random

with open("blog_access.log", "w") as fout:
    date_list = ["2019-01-01", "2019-01-02", "2019-01-03"]
    page_ids = [1001, 1002, 1003]
    user_id_min = 1
    user_id_max = 1000
    events = ["show", "click"]

    # 生成10万条数据
    for i in range(10 * 10000):
        pdates = date_list[random.randint(0, 2)].split("-")
        date_obj = datetime.datetime(int(pdates[0]), int(pdates[1]), int(pdates[2]), 0, 0, 0)
        date_delta = datetime.timedelta(seconds=random.randint(1, 86400 - 1))
        new_date = str((date_obj + date_delta).strftime("%Y-%m-%d %H:%M:%S"))

        user_id = random.randint(user_id_min, user_id_max)
        page_id = page_ids[random.randint(0, 2)]
        event = events[random.randint(0, 1)]

        out_fields = [
            new_date, user_id, page_id, event
        ]

        fout.write("\t".join([str(x) for x in out_fields]) + "\n")
