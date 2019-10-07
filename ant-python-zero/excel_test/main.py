
import xlwt

workbook = xlwt.Workbook(encoding="utf-8")

sheet = workbook.add_sheet("学生成绩表")

row = 0

with open("input.txt") as fin:
    for line in fin:
        line = line.strip()
        fields = line.split("\t")
        for col, value in enumerate(fields):
            sheet.write(row, col, value)
        row += 1

workbook.save("学生成绩表.xls")
