import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

#TODO - replace list of comparisonStocks with user input/choice
comparisonStocks = ['MSFT', 'NVDA', 'AAPL', 'NFLX', 'TSLA']
baseStock = 'SPY'

#currently unused
class backtesting:
    def __init__(self) -> None:
        self.shmoney = 1000000
        self.portfolio = {}
        self.default_qty = 0
        pass
    
    #accept stock dataframe and buy condition, return win rate, p/l, sharpe etc
    #def backtest(self, df, buy_condition, sell_condition):

#currently unused
class paperTrading:
    def __init__(self) -> None:
        pass

    #functions for live trading with fake money
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

    # add column relStr vs SPY
    def relativeStrength(df):
        df['relStr'] = SPY['pctMove'].sub(df['pctMove'])

    #add moving average of selected column (dataColumn) to dataframe in new column (columnName)
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
