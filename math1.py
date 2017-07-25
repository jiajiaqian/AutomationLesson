import math
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]  #list类型
y = []   #预留一个list类型
for i in x:
    y.append(math.exp(i)+10+math.sin(i)+math.pow(i,4))

print(y)
#调用figure创建一个绘图对象，并且使它成为当前的绘图对象。
#通过figsize参数可以指定绘图对象的宽度和高度，单位为英寸；
plt.figure(figsize=(8,4))
plt.plot(x,y)
plt.show()


