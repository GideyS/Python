'''
Surafeal G Meshesha
5/20/2022
ICT- 4370-1(Python Programming)
Week-8 Data Visualization
This program imports data from multiple files(csv and Json)
to calculate the total closing value of the stocks multiple dates
of valuation. The program uses Tkinter GUI to open the CSV, JSON files and 
locate the path for the programs output.
Furthermore, this program will display the change of each stocks
in a graphical presentation using Matplotlib

'''
from module import *
import csv
import json
import matplotlib.pyplot as plt
import tkinter as tk

#trying to run the file class from the module and the tkinter module
try:
    # Init FileControl object to store paths
    file_control = FileControl()

    # Open tkinter GUI for user
    window = tk.Tk()
    # Default window size/title
    window.geometry('300x300')
    window.title('Open File')

    # Create and pack CSV selection button
    profile_button = tk.Button(window, text = "Please Select Stock CSV file", 
                    command=file_control.set_portfolio_path)
    profile_button.pack(pady=20)

    # Create and pack JSON selection button
    information_button = tk.Button(window, text = "Please Select the JSON File", 
                        command=file_control.set_information_path)
    information_button.pack(pady=20)

    # Create and pack PNG output selection button
    output_button = tk.Button(window, text = "Please Select the path and create \n a file name for the output",
                        command=file_control.set_output_path)
    output_button.pack(pady=20)

    # Create and pack Submit button, which closes tkinter GUI
    exit_button = tk.Button(window, text="Submit", command=window.destroy)
    exit_button.pack(pady=20)

    # Keeps tkinter window open until exit_button is clicked
    window.mainloop()

    
    # Error message if the file path or the file selected is incorrect
    if not file_control.paths_exist():
        print ('File paths not populated correctly. Application will close')

    

    # Create Investor object
    investor = Investor('Bob Smith')

    # Read in CSV
    with open(file_control.get_portfolio_path(), mode='r') as csv_file:
        stock_csv = csv.DictReader(csv_file)
        for stock in stock_csv:
            # Instantiate a Stock object for each row in the CSV
            try:
                stock_obj = Stock(stock['SYMBOL'], stock['NO_SHARES'])
            except:
                print ('Error creating Stock object')

            # Add the stock object to the investor object
            investor.add_stock(stock_obj)

    # Set stock metadata (unique names and share numbers)
    investor.set_stock_metadata()

    # Open stock date json file
    with open(file_control.get_information_path()) as f:
        data = json.load(f)

    # Iterate dicts in file
    for row in data:
        stockSymbol = row['Symbol']
        date = row['Date']
        open_price = row['Open']
        high_price = row['High']
        low_price = row['Low']
        closingPrice = row['Close']
        volume = row['Volume']

        investor.add_stock_timestamp(Stock_Timestamp(stockSymbol, date, closingPrice))

    # Format the data into matplotlib
    data = investor.prep_for_graph()

    
    f = plt.figure()
    f.set_figwidth(10)
    f.set_figheight(6)

    plt.title("Historical Stock Data")

    plt.xlabel('Stock Valuation Dates')

    plt.ylabel('Stock Closing Prices in Dollars')
    

    # Define X axis as dates and remove from dict
    x = data['dates']
    data.pop('dates')
    # Iterate each stock list and create a plot line
    for key, value in data.items():
        
        plt.plot(x, value, label=key)

    # Format X axis dates
    plt.gcf().autofmt_xdate()
    # Add legend
    plt.legend(loc='upper left')
    # Save plot to disk as PNG
    plt.savefig(file_control.get_output_path())

except:
    print('An error occured')
    
