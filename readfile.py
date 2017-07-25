path = 'D:/post/test.txt'  #要读取文件的路径
fr = open(path)   #打开这个文件
lineArr = []      #预留空变量
for line in fr.readlines():   #循环读取文件的每一行
    # 将文件中的每一行以‘空格’为中断符号
    curLine = line.strip().split('\t')
    # 将一行中的信息存储至lineArr
    lineArr.append(curLine)
fr.close()
#print(lineArr)

print(lineArr[1])