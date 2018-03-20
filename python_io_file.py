# -*- coding:utf-8 -*-
#
# Author : hhl
#
# Time : 二 20 3月 2018 11:31:06
#
#

# 打开文件
file_obj = open(txt_filename, 'r', encoding='utf-8')
# 读取整个文件内容
all_content = file_obj.read()
# 逐行读取
line1 = file_obj.readline()
# 全部读出
lines = file_obj.readlines()
for i, line in enumerate(lines):
    print ('{}: {}'.format(i, line))
# 关闭文件
file_obj.close()




#打开写文件
file_obj = open(txt_filename, 'w', encoding='utf-8')
# 写入全部内容
file_obj.write("《Python数据分析》")
# 写入字符串列表
lines = ['这是第%i行iiiii\n' %n for n in range(100)]
file_obj.writelines(lines)
file_obj.close()




#with 方式可以自动关闭文件
with open(txt_filename, 'r', encoding='utf-8') as f_obj:
    print(f_obj.read())


