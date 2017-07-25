import numpy as np
from sklearn import datasets, linear_model

diabetes = datasets.load_diabetes()
# 查看第一列年龄的数据
print(diabetes.data[0])  #第一个病人的10项数据
#请注意，以上的数据是经过特殊处理， 10个数据中的每个都做了均值中心化处理，然后又用标准差乘以个体数量调整了数值范围。
# 验证就会发现任何一列的所有数值平方和为1.

# 糖尿病进展的数据
print(diabetes.target)  # 数值介于25到346之间

# 只使用一个变量
#diabetes_X = diabetes.data[:, np.newaxis, 2] #np.newaxis 在使用和功能上等价于 None
diabetes_X = diabetes.data

# 切分训练集与测试集
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# 创建线性回归
regr = linear_model.LinearRegression()
'''
regr = linear_model.Lasso(alpha=0.1, copy_X=True, fit_intercept=True, max_iter=1000,
                          normalize=False, positive=False, precompute=False,
                          random_state=None,selection='cyclic', tol=0.0001, warm_start=False)
'''
# 用训练集训练模型
regr.fit(diabetes_X_train, diabetes_y_train)

# 对每个特征绘制一个线性回归图表
import matplotlib.pyplot as plt
# 调用预测模型的coef_属性,求出每种生理数据的回归系数b
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
# 如何评价以上的模型优劣呢？我们可以引入方差，方差越接近于1,模型越好.
# 方差: 统计中的方差（样本方差）是各个数据分别与其平均数之差的平方的和的平均数
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))
#Mean squared error: 2548.07
#Variance score: 0.47

# Plot
#plt.scatter(diabetes_X_test, diabetes_y_test,  color='black') #画出散点图
#plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
         #linewidth=3) #画出直线
#plt.show()  #显示图像