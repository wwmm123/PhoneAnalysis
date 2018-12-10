# coding=utf-8
'''
替换脚本中的内容
'''

import os

# fp_read = open('ReadMe.txt', 'rb') #手机号
# lines = fp_read.readlines()
# fp_read.close()
# flag = 0
# for index in range(len(lines)):
# 	print lines[index]
# 	if(lines[index].find("try")):
# 		print index
# 		lines.insert(index, 'a new line')  # 在第二行插入
# 		flag = 1
# 		break
# if flag:
# 	print 90809
# 	# s = join(lines)
# 	fp_write = open('Read.txt', 'wb')
# 	for i in lines:
# 		fp_write.write(i)
# 	fp_write.close()
# else:
# 	pass











#
fileold = open("demo.py", "rb+")
configfile_list = fileold.readlines()

print "length:",configfile_list.__len__()
tarline=0
for line in configfile_list:
	line_new = line.replace('a','b')
	fileold.write(line_new)
fileold.close()
# for i in range(configfile_list.__len__()):
# 	if configfile_list[i].__contains__("a"):
# 		# tarline = int(i)
# 		print 888
# 		configfile_list[i].replace("a", "666")
# 		print configfile_list[i]

# print "add <cman two_node=**** at line:",tarline
# addinfo = '\t' + "print 'hello'" + '\n'
# configfile_list.insert(tarline,addinfo)


# print "length of cluster.conf after change:",configfile_list.__len__()
# filenew= open("demo.py","wb")
# for item in configfile_list:
# 	filenew.write(item)
# filenew.close()













