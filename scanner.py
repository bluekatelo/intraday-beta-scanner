import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

#todo - replace with accepting input for comparison stocks, also currently unusued
comparisonStocks = ['MSFT', 'NVDA', 'AAPL', 'NFLX', 'TSLA']
baseStock = 'SPY'

class backtesting:
    def __init__(self) -> None:
        pass

    def backtest(self, df, buy_condition, sell_condition):
        self.shmoney = 1000000
        self.portfolio = {}
        self.default_qty = 0

    #accept stock dataframe and buy condition, return win rate, p/l, sharpe etc

class paperTrading:
    def __init__(self) -> None:
        pass

    #def buy(ticker, quantity):
    #def sell(ticker, quantity):

class dfFuncs:
    def __init__(self) -> None:
        pass

    #create pandas dataframe from a given stock ticker string
    def makeStock_df(ticker):
        ticker = yf.Ticker(ticker)
        return ticker.history(period="1d", interval="1m")

    # assign to new column = subtract by 1st open price, divide by first open price
    def pct_move_from_open(df):
        df['pctMove'] = ((df['Close'] - df.iloc[0, 0]) / df.iloc[0, 0]) * 100


    def relativeStrength(df):
        df['relStr'] = SPY['pctMove'].sub(df['pctMove'])

    #add moving average column to dataframe
    def ma(df, columnName, dataColumn, span):
        df[columnName] = df[dataColumn].rolling(span).mean()

#create SPY dataframe
SPY = dfFuncs.makeStock_df('SPY')
dfFuncs.pct_move_from_open(SPY)
SPY.to_excel('C:\\Python\\simple_relativeStrength\\dataframes\\SPY.xlsx' , index = False, header=True)

#create dataframes for all comparisonStocks
for i in comparisonStocks:
    df = dfFuncs.makeStock_df(i)
    dfFuncs.pct_move_from_open(df)
    path = "C:\\Python\\simple_relativeStrength\\dataframes\\%s.xlsx" % i
    df.to_excel(path, index = False, header=True)

#MSFT = pd.read_excel("C:\\Python\\simple_relativeStrength\\dataframes\\MSFT.xlsx")


#old pct_move function

"""
def pct_move_from_open(df):
    lst = list(df['Close'])
    pctMoves = []
    for i in lst:
        pctMoves.append(round(((i - lst[0]) / lst[0])*100, 3))
    df['pctMove'] = pctMoves
"""