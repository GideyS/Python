import csv
import json
from datetime import datetime,date

stock_file=open('AllStocks.json')
stockData=json.load(stock_file)
numshareFile=open('Lesson6_Data_Stocks.csv')
sharesFile=csv.reader(numshareFile)
print(stockData)


class Stock:
    def __init__(self,stockSymbol,stockDate,closingPrice,numShares = 0):
        #initiating Dog class
        self.stockSymbol=stockSymbol
        self.stockDate=stockDate
        self.closingPrice=closingPrice
        self.numShares=numShares
        self.closingList=[]
        self.dateList=[]
        self.newValue=[]


    def addStock (self,stockDate,closingPrice):
        self.closingList.append(closingPrice)
        self.dateList.append(stockDate)


    def calculateValue(self,numShares,closingList,newValue,value):
        value=numShares*closingList
        newValue.append(value)

    def __str__(self):
        print(self.stockSymbol, self.stockDate)

        

stockDictionary={}
for data in stockData:
    if data['Symbol'] not in stockDictionary:
        newStock=Stock(data['Symbol'],data['Date'],data['Close'])
        stockDictionary[data['Symbol']] = newStock
    else:
        stockDictionary[data['Symbol']].closingPrice=data['Close']
    stockDictionary[data['Symbol']].addStock(data['Close'],
        datetime.strptime(data["Date"],'%d-%b-%y'))

Stock.__str__()
