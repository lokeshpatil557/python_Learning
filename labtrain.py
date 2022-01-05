
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
a=pd.read_csv("C:/Users/Lokesh/Desktop/cdac ai material/machine learning/29dec/Train.csv")
print(a.head())
print(a.info())
a['Datetime']=pd.to_datetime(a['Datetime'])
print(a.info())
a.drop('ID',axis=1,inplace=True)
print(a.info())
a.set_index('Datetime',inplace=True)
print(a.head())
print(a.tail)
print(a.describe())
a.plot()
plt.show()
#Moving Average
a['AMA_12']=a.Count.rolling(12,min_periods=1).mean()
a['SMA_24']=a.Count.rolling(24,min_periods=1).mean()
print(a.head(20))
a.plot()
plt.show()
#Exponential Moving Average
a['EMA_0.1']=a.Count.ewm(alpha=0.1,adjust=False).mean()
a['EMA_0.3']=a.Count.ewm(alpha=0.3,adjust=False).mean()
print(a.head())
a.plot()
plt.show()

#Check for Stationary
rolmean = a.Count.rolling(window=12).mean()
rolstd = a.Count.rolling(window=12).std()

orig = plt.plot(a.Count,color='blue',label='original')
mean = plt.plot(rolmean,color='red',label='Rolling Mean')
std = plt.plot(rolstd,color='black',label='Rolling std')
plt.legend()
plt.title('Rolling mean and Std deviation')
plt.show()

#Adfuller State

from statsmodels.tsa.stattools import adfuller
test_result=adfuller(a['Count'])
print(test_result)








