from matplotlib import pyplot as py
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r"/System/Library/Fonts/PingFang.ttc")
x = [34, 56, 78, 15, 65, 54, 15, 23, 23, 45, 26, 75, 46, 67, 52, 65, 42, 53, 34, 45, 42, 68, 57, 79]
b = 8
d = (max(x) - min(x)) // b
py.figure(figsize=(20, 8), dpi=80)

py.hist(x, d, color='orange', density=True)
py.xticks(range(min(x), max(x) + d, d))
py.xlabel('票房区间', fontproperties=my_font)
py.ylabel('区间数量', fontproperties=my_font)

py.grid(alpha=0.3)
py.show()
py.savefig('./直方图.png')
