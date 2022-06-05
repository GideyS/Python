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
import copy
import datetime
import os
import tkinter.filedialog


class Stock_Timestamp():
    #Class to hold stock timestamp information

    def __init__(self, symbol, date, close_price):
        self.symbol = symbol
        self.date = datetime.datetime.strptime(date, "%d-%b-%y")
        self.close_price = float(close_price)


class Stock():
    #Class to hold Stock objects

    def __init__(self, symbol, number_of_shares):
        self.symbol = symbol
        # Convert necessary string fields to float
        self.number_of_shares = float(number_of_shares)


class Investor():
    #Creating Investor class to hold Stock objects

    def __init__(self, name):
        self.name = name
        self.stocks = {}
        self.stock_timestamps = {}
        self.stock_volumes = {}
        self.symbol_dict = {}

    def add_stock(self, stock):
        #Add new stock to stocks dictionary
        self.stocks[stock.symbol] = stock

    def set_stock_metadata(self):
        #Function to capture a list of all unique stocks and the number of owned shares per stock'''
        for key, value in self.stocks.items():
            self.stock_volumes[key] = value.number_of_shares

        symbol_set = set(self.stocks.keys())
        for i in symbol_set:
            self.symbol_dict[i] = None

    def calculate_value(self, symbol, close):
        #Calculate the value of a stock (closing price * number of shares)
        num_shares = self.stock_volumes[symbol]
        return num_shares * close

    def add_stock_timestamp(self, timestamp):
        #Add a stock timestamp to the investor portfolio

        # Only process data that the investor owns
        if timestamp.symbol in self.symbol_dict:
            # Calculate the value of the stock on this date
            value = self.calculate_value(
                timestamp.symbol, timestamp.close_price)

            # If a dictionary entry for this date does not exist, create it
            if timestamp.date not in self.stock_timestamps:
                # Deepcopy the default stock dictionary, prepopulated with None values
                self.stock_timestamps[timestamp.date] = copy.deepcopy(
                    self.symbol_dict)

            # Populate the value of the stock on this date
            self.stock_timestamps[timestamp.date][timestamp.symbol] = value

    def prep_for_graph(self):
        # Sort dates to ensure proper order
        sorted_dates = sorted(self.stock_timestamps)

        # Create a dictionary where the values are lists, with an entry for each stock
        # and an entry for dates
        graph_dict = {}
        graph_dict['dates'] = []
        for key in self.symbol_dict.keys():
            # Init list for each stock
            graph_dict[key] = []

        for date in sorted_dates:
            graph_dict['dates'].append(date)
            # Iterate through each stock value on this date and populate the proper lists
            for key, value in self.stock_timestamps[date].items():
                graph_dict[key].append(value)

        return graph_dict

class FileControl():
    #Creating the file class to hold and maintain file paths

    def __init__(self):
        self.stock_portfolio_path = None
        self.stock_information_path = None
        self.output_path = None
        self.own_path = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def paths_exist(self):
        #Function to determine if all required data was entered

        if (self.stock_information_path != None and self.stock_portfolio_path != None
                and self.output_path != None):
            return True
        return False

    def set_portfolio_path(self):
        #Set path to Stock portfolio CSV file

        # Prompt the dialogbox to only show CSV files
        path = tkinter.filedialog.askopenfilename(initialdir=self.own_path, filetypes=[('CSV Files', '*.csv')])
        self.stock_portfolio_path = path

    def get_portfolio_path(self):
        return self.stock_portfolio_path

    def set_information_path(self):
        #Set path to portfolio CSV

        # Prompt filename dialog in working dir, only show JSON files
        path = tkinter.filedialog.askopenfilename(initialdir=self.own_path, filetypes=[('JSON Files', '*.json')])
        self.stock_information_path = path

    def get_information_path(self):
        return self.stock_information_path

    def set_output_path(self):
        #Set path to output PNG

        # Prompt filename dialog in working dir, require save as PNG
        path = tkinter.filedialog.asksaveasfilename(initialdir=self.own_path, filetypes=[('PNG Files', '*.png')])
        self.output_path = path

    def get_output_path(self):
        return self.output_path