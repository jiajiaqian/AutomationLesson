from sklearn.linear_model import RandomizedLasso
import pandas
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

# load dataset
dataframe = pandas.read_csv("test2.csv")
print(len(dataframe))

readLine=['LENGTH', 'WIDTH', 'GAUGE', 'TEMP_WATER', 'SPEED', 'ACCELERATION', 'REAL_TOTAL_FLOW'
          , 'AVECR','TEMP_ENTRY_SURF_UP', 'TEMP_EXIT_SURF_UP', 'TEMP_EXIT_SURF_DOWN'
          , 'TEMP_EXIT_AVG', 'ACC_RATIO_6', 'C_VAL', 'CR_VAL', 'CU_VAL', 'MN_VAL', 'MO_VAL'
          , 'NI_VAL', 'SI_VAL', 'TI_VAL', 'NB_VAL', 'B_VAL', 'V_VAL', 'YP_RST', 'TS_RST', 'EL_RST']

readLine2 = ['TEMP_EXIT_AVG','SPEED']
readLine3 = ['FINISH_ROLL_TEMP', 'LENGTH', 'WIDTH', 'GAUGE', 'TEMP_WATER', 'C_VAL', 'CR_VAL', 'CU_VAL', 'MN_VAL', 'MO_VAL'
          , 'NI_VAL', 'SI_VAL', 'TI_VAL', 'NB_VAL', 'B_VAL', 'V_VAL', 'YP_RST', 'TS_RST', 'EL_RST','ROLLING_PASS','SLAB_GAUGE']

inputX = dataframe[readLine3].values
outputY = dataframe[readLine2].values

x_train, x_test, y_train, y_test = train_test_split(inputX, outputY, test_size=0.3, random_state=2)

from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression

#rlasso = Lasso(alpha=0.01)
#rlasso = LinearRegression()

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
#rlasso = AdaBoostRegressor(DecisionTreeRegressor(max_depth=5), n_estimators=50)

from sklearn.ensemble import ExtraTreesRegressor

rlasso2 = ExtraTreesRegressor(n_estimators=300, max_features='auto',
                                       random_state=0)

rlasso2.fit(x_train, y_train)

yPre2 = rlasso2.predict(x_test)
print(rlasso2.feature_importances_)

'''
print("Mean squared error test2: %.2f"
      % np.mean( (yPre2[:, 0] - y_test[:, 0]) ** 2))
print("Mean squared error test2: %.2f"
      % np.mean( (yPre2[:, 1] - y_test[:, 1]) ** 2))
'''

print("Mean squared error test2: %.2f"
      % np.mean( (yPre2 - y_test) ** 2))
print('Variance score rlasso 2: %.2f' % rlasso2.score(x_test, y_test))



'''
print("Mean squared error test: %.2f"
      % np.mean((rlasso.predict(x_test) - y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % rlasso.score(x_test, y_test))

print("Mean squared error train: %.2f"
      % np.mean((rlasso.predict(x_train) - y_train) ** 2))
print('Variance score: %.2f' % rlasso.score(x_train, y_train))

#print(rlasso.coef_)

import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(y_test[:], 'r.', markersize=12)
plt.plot(rlasso.predict(x_test[:]), 'g.-', markersize=12)
#plt.legend(('Data', 'Isotonic Fit', 'Linear Fit'), loc='lower right')
#plt.title('Isotonic regression')
plt.show()
'''


