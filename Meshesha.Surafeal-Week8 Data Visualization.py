
'''
Surafeal G Meshesha
5/20/2022
ICT- 4370-1(Python Programming)
Week-8 Data Visualization
This program imports data from multiple files(csv and Json)
to calculate the total closing value of the stocks multiple dates
of valuation. Furthermore, this program will display the change of each stocks
in a graphical presentation.
'''
#importing libraries and everything from the Week8Module
from Week8Module import *
import pandas as pd
import json
import matplotlib.pyplot as plt


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
    #print(numShares)
except:
    print("Error while reading Stock Data File: please check the file path")

#loading the values from the Json file to stock Dictionary    
try:
    with open('AllStocks.json') as f:
        stocks = json.load(f)  # loaded data into the stocks dictionary
except:
    print("Error while loading file: Please check the file path")
    

# Calculating the AIG valuation
aigDates = []
aigPrices = []
aigValue=[]
for i in stocks:
    if i['Symbol'] == 'AIG':
        aigDates.append(i['Date'])
        aigPrices.append(i['Close'])
i=0
for value in aigPrices:
    value=aigPrices[i]*numShares[3]
    aigValue.append(value)
    i=i+1
    
# Ordering the values and dates 
aigDates = aigDates[::-1]
aigvalue = aigValue[::-1]

# Calculating the F valuation
FDates = []
FPrices = []
FValue=[]
for i in stocks:
    if i['Symbol'] == "F":
        FDates.append(i['Date'])
        FPrices.append(i['Close'])

i=0
for value in FPrices:
    value=FPrices[i]*numShares[6]
    FValue.append(value)
    i=i+1
    
FDates = FDates[::-1]
FValue = FValue[::-1]


# Calculating the FB valuation
FBDates = []
FBPrices = []
FBValue=[]
for i in stocks:
    if i['Symbol'] == 'FB':
        FBDates.append(i['Date'])
        FBPrices.append(i['Close'])
i=0
for value in FBPrices:
    value=FBPrices[i]*numShares[4]
    FBValue.append(value)
    i=i+1
    
FBDates = FBDates[::-1]
FBValue = FBValue[::-1]

# Calculating the GOOGLE valuation
GOOGDates = []
GOOGPrices = []
GOOGValue=[]
for i in stocks:
    if i['Symbol'] == 'GOOG':
        GOOGDates.append(i['Date'])
        GOOGPrices.append(i['Close'])
i=0
for value in GOOGPrices:
    value=GOOGPrices[i]*numShares[0]
    GOOGValue.append(value)
    i=i+1
    
GOOGDates = GOOGDates[::-1]
GOOGvalue = GOOGValue[::-1]

# Calculating the IBM valuation
IBMDates = []
IBMPrices = []
IBMValue=[]
for i in stocks:
    if i['Symbol'] == 'IBM':
        IBMDates.append(i['Date'])
        IBMPrices.append(i['Close'])
i=0
for value in IBMPrices:
    value=IBMPrices[i]*numShares[7]
    IBMValue.append(value)
    i=i+1
    

IBMDates = IBMDates[::-1]
IBMvalue = IBMValue[::-1]

# Calculating the M valuation
MDates = []
MPrices = []
MValue=[]
for i in stocks:
    if i['Symbol'] == 'M':
        MDates.append(i['Date'])
        MPrices.append(i['Close'])

i=0
for value in MPrices:
    value=MPrices[i]*numShares[5]
    MValue.append(value)
    i=i+1

MDates = MDates[::-1]
Mvalue = MValue[::-1]

# Calculating the MSFT valuation
MsftDates = []
MsftPrices = []
MsftValue=[]
for i in stocks:
    if i['Symbol'] == 'MSFT':
        MsftDates.append(i['Date'])
        MsftPrices.append(i['Close'])
i=0
for value in MsftPrices:
    value=MsftPrices[i]*numShares[1]
    MsftValue.append(value)
    i=i+1


Msftdates = MsftDates[::-1]
Msftvalue = MsftValue[::-1]

# Calculating the RDSA valuation
RdsaDates = []
RdsaPrices = []
RdsaValue=[]
for i in stocks:
    if i['Symbol'] == 'RDS-A':
        RdsaDates.append(i['Date'])
        RdsaPrices.append(i['Close'])
i=0
for value in RdsaPrices:
    value=RdsaPrices[i]*numShares[2]
    RdsaValue.append(value)
    i=i+1
    
RdsaDates = RdsaDates[::-1]
RDSAvalue = RdsaValue[::-1]


#
dates = [aigDates[0], aigDates[50], aigDates[100], aigDates[150],
        aigDates[200], aigDates[250], aigDates[300], aigDates[350],
        aigDates[400], aigDates[450], aigDates[-1]]


#ploting the dates and values for data visualization
#adjusting the chart size
f = plt.figure()
f.set_figwidth(10)
f.set_figheight(6)


plt.plot(GOOGDates, GOOGvalue, label="GOOG")

plt.plot(MsftDates, MsftValue, label="MSFT")

plt.plot(RdsaDates, RDSAvalue, label="RDSA")

plt.plot(aigDates, aigvalue, label="AIG")

plt.plot(FBDates, FBValue, label="FB")

plt.plot(MDates, MValue, label="M")

plt.plot(FDates, FValue, label="F")

plt.plot(IBMDates, IBMValue, label="IBM")

#printing the dates on the X axis
plt.xticks(dates, rotation=40)
plt.legend(loc='upper left')

#Visualizing the data
#plt.show()
#Saving the graphs to a file
plt.savefig('Meshesha.Surafeal-Data Visualization.png')