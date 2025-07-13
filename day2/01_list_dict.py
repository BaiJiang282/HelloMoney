# ★ 定义一个列表，里面放 3 个“学生成绩表”
students = [
    {'name': 'Tom', 'score': 95},
    {'name': 'Jerry', 'score': 88},
    {'name': 'Spike', 'score': 77}
]

# ★ 计算平均分
# sum(...) 把每个学生的 score 加起来
# len(students) 数列表里有几个学生
avg = sum(s['score'] for s in students) / len(students)

# ★ 打印结果，:.2f 表示保留两位小数
print(f"平均分：{avg:.2f}")