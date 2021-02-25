"""
根据正则匹配路径下所有符合规则的文件名，笔记
filename1 = 'D:/Google/'
b = []
for i in os.listdir(filename1):    #列出路径下所有的文件名
    ret = re.search(r"^PC-[a-z0-9]{6}(-[0-9]{4})$", i)    #正则匹配，例如PC-abc123-1234
    if ret:
        # print(ret)      打印匹配的文件名
        #以空格来区分
        msg = i.split(' ')
        # print(msg[0])
        #将匹配的文件名加入到新列表里
        b.append(msg[0])
    else:
        continue

"""
from time import sleep
import os
import re

filename = 'D:/Google/Logs/'
f = open(filename+'test.log', encoding='gbk')
f1 = open(filename+'filematch.log','w',encoding='gbk')

s = input("输入你要查询的关键字：")
i = 0
while True:
    # 使用readline（）读文件
    line = f.readline()
    i += 1
    if line:
        if s not in line:
            continue
        else:
            print("当前行数%d"%i,line, end='')
            f1.write(line)
            sleep(1)                  #可不要
    else:
        break

f.close()
f1.close()