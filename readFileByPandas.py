import pandas
path = 'D:/post/test.xlsx'  #要读取文件的路径
#dataframe = pandas.read_csv(path, delim_whitespace=True, encoding="gbk")  #读取txt、csv文件
dataframe = pandas.read_excel(path)  #读取excel文件

#print(dataframe)
#print(dataframe.columns)
#print(dataframe.index)
print(dataframe.values)
