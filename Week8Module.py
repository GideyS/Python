import json
from datetime import datetime,date
import pandas as pd


#creating empty dictionary and list
stocks = {}
numShares=[]

#reading the values from the csv file and creating data frames
try:
    stockFile = pd.read_csv('Lesson6_Data_Stocks.csv')
    stockdata=pd.DataFrame(stockFile)

    numshare=stockdata['NO_SHARES']
    stockSymbol=stockdata['SYMBOL']

#extracting the values from dataframe to list for ease of calculations
    for i in numshare:
        numShares.append(i)
    print(numShares)
except:
    print("Error while reading Stock Data File: please check the file path")
try:
    with open('AllStocks.json') as f:
        stocks = json.load(f)  # loaded data into the stocks dictionary
except:
    print("Error while loading file: Please check the file path")
    
class Stock:
    def __init__(self,stockSymbol,stockDate,closingPrice):
        #initiating Dog class
        self.stockSymbol=stockSymbol
        self.stockDate=stockDate
        self.closingPrice=closingPrice
        self.closingList=[]
        self.dateList=[]
    def addStock (self,stockDate,closingPrice):
        self.closingList.append(closingPrice)
        self.dateList.append(stockDate)
        