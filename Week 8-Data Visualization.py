from Week8Module import *
from datetime import datetime,date
import matplotlib.pyplot as plt
import matplotlib
from itertools import cycle



stockDictionary={}
for data in stockData:
    if data['Symbol'] not in stockDictionary:
        newStock=Stock(data['Symbol'],data['Date'],data['Close'])
        
        stockDictionary[data['Symbol']]=newStock
    else:
        stockDictionary[data['Symbol']].closingPrice=data['Close']
    stockDictionary[data['Symbol']].addStock(data['Close'],
        datetime.strptime(data["Date"],'%d-%b-%y'))
cycol = cycle('bgrcmk')  
#print(stockDictionary)
value = []
dates = []
name = []
for data in stockDictionary:
    value.append(stockDictionary[data].closingPrice)
    dates.append(stockDictionary[data].dateList)
    #dates.append(matplotlib.dates.date2num(stockDictionary[data].dateList))
    name.append(stockDictionary[data].stockSymbol )
'''plt.figure()
plt.plot(value, dates, marker='None', linestyle='solid')#,label=name,c=next(cycol))
       # Adding the title
plt.title("Data Visualization")
    # Adding the labels
plt.ylabel("Value")
plt.xlabel("Date")
plt.legend()
plt.show()'''