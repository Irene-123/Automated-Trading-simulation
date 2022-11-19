import pandas as pd 
import matplotlib.pyplot as plt 
import requests
import math
from termcolor import colored as cl 
import numpy as np
import os 
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (15, 8)

class trader: 
    def __init__(self) -> None:
        try: 
            df= pd.read_csv(r'C:\Users\kirti\Automated Trading_simulation\static\ohlc.csv')
        except FileNotFoundError as e: 
            raise Exception("The file could not be located") 
        self.df= df
    def clean_data(self): 
        self.df= self.df[['Datetime', 'Open', 'Close', 'High', 'Low', 'Volume']]
        self.df = self.df.set_index('Datetime')
        self.df.to_csv('msft.csv')
        self.df = pd.read_csv('msft.csv')
        os.remove('msft.csv')
        self.df['Datetime']= pd.to_datetime(self.df['Datetime'])
        def sma(data, n):
            sma = data.rolling(window = n).mean()
            return pd.DataFrame(sma)

        n = [20, 50]
        for i in n:
            self.df[f'sma_{i}'] = sma(self.df['Close'], i)
        self.df['sma_20'].fillna(0, inplace=True)
        self.df['sma_50'].fillna(0, inplace=True)
        self.df['sma_20'].apply(lambda a:"{0:.10f}".format(a))
        self.df['sma_50'].apply(lambda a:"{0:.10f}".format(a))
        # print(self.df)
    def strategy(self): 
        sma1 =  self.df['sma_20']
        sma2= self.df['sma_50']
        buy_price = []
        sell_price = []
        sma_signal = []
        signal = 0
        for row,s, t in zip(self.df.iterrows(), sma1, sma2):
            if s > t:
                if signal != 1:
                    buy_price.append(row)
                    sell_price.append(np.nan)
                    signal = 1
                    sma_signal.append(signal)
                else:
                    buy_price.append(np.nan)
                    sell_price.append(np.nan)
                    sma_signal.append(0)
            elif t > s:
                if signal != -1:
                    buy_price.append(np.nan)
                    sell_price.append(row)
                    signal = -1
                    sma_signal.append(-1)
                else:
                    buy_price.append(np.nan)
                    sell_price.append(np.nan)
                    sma_signal.append(0)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                sma_signal.append(0)
                
        return buy_price, sell_price, sma_signal

    def plot(self, buyprice, sellprice): 
        msft= self.df.copy() 
        plt.plot(msft['Close'], alpha = 0.3, label = 'MSFT')
        plt.plot(msft['sma_20'], alpha = 0.6, label = 'SMA 20')
        plt.plot(msft['sma_50'] , alpha = 0.6, label = 'SMA 50')
        plt.scatter(msft.index, buyprice, marker = '^', s = 200, color = 'darkblue', label = 'BUY SIGNAL')
        plt.scatter(msft.index, sellprice , marker = 'v', s = 200, color = 'crimson', label = 'SELL SIGNAL')
        plt.legend(loc = 'upper left')
        plt.title('MSFT SMA CROSSOVER TRADING SIGNALS')
        plt.savefig("{% static 'plot.png' %}")
        plt.show()
    
    def create_position(self): 
        msft= self.self.df.copy() 
        position = []
        for i in range(len(signal)):
            if signal[i] > 1:
                position.append(0)
            else:
                position.append(1)
                
        for i in range(len(msft['close'])):
            if signal[i] == 1:
                position[i] = 1
            elif signal[i] == -1:
                position[i] = 0
            else:
                position[i] = position[i-1]
                
        sma_20 = pd.DataFrame(sma_20).rename(columns = {0:'sma_20'})
        sma_50 = pd.DataFrame(sma_50).rename(columns = {0:'sma_50'})
        signal = pd.DataFrame(signal).rename(columns = {0:'sma_signal'}).set_index(msft.index)
        position = pd.DataFrame(position).rename(columns = {0:'sma_position'}).set_index(msft.index)

        frames = [sma_20, sma_50, signal, position]
        strategy = pd.concat(frames, join = 'inner', axis = 1)
        strategy = strategy.reset_index().drop('date', axis = 1)

        return strategy
        
obj= trader() 
obj.clean_data() 
buy_price, sell_price, signal = obj.strategy()

print(signal.count(1))
print(signal.count(-1))