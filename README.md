# Problem statement

Trading stock market is a tricky business and there is rarely a single investor who
becomes successful without experience and practicing. Traditional architecture
of trading involves human emotions, blunders and investing without knowledge.
This results in loss of money and human efforts. Automated trading invests based
on machine learning model and past data, doesn’t have emotions and only makes
decisions by looking at numbers. Today, trading is done using automated machine
learning algorithms but it can’t be always accurate, we need a measure on how
the algorithm is accurate because HFT’s spend crores of money in stocks and they
need a precise algorithm which does the automated trading. <br>
A stock market simulator will simulate the stock just like a real-time stock and
an automated trading algorithm attached to it will buy and sell stocks. Using a
stock market simulator, it allows one to practice the art of trading while learning
on historical data or real-time data using virtual money.

## Implementation of combined ADX + RSI Strategy

```
ADX > 35 AND RSI < 50 AND +DI < −DI ==> BUY SIGNAL
ADX > 35 AND RSI > 50 AND +DI > −DI ==> SELL SIGNAL
```

## Implementation of Backtesting. 

Backtesting is the process of seeing how well our trading strategy has performed
on the given stock data. In our case, we are going to implement a backtesting
process for our ADX and RSI combined trading strategy over the S&P 500 stock
data.
 We are going to backtest our strategy by
investing a 100k $ into our trading strategy. So first, we are storing the amount
of investment into the ‘investment value’ variable. After that, we are calculating
the number of S&P 500 stocks we can buy using the investment amount.

![backtesting](https://user-images.githubusercontent.com/58950467/210149384-40981068-809f-4f6e-9334-ac1e99d9c39c.png)

# System Integration to Django website.


![homepage](https://user-images.githubusercontent.com/58950467/210149425-ae4da649-9994-4188-b7dd-81c1f51c7d2b.png)


![trade](https://user-images.githubusercontent.com/58950467/210149426-f545e16f-55e1-49af-ac6c-c4a8d5446c18.png)

## Results



![results2](https://user-images.githubusercontent.com/58950467/210149444-890ab3a7-3c5e-4891-ad20-47244bc1adea.png)
