import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

#######################################################################################################
# CONVERTING DATES FROM 'GIBBERISH' TO VALID MATPLOTLIB DATA FORMAT

def bytesupdate2num(fmt, encoding = 'utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_data(stock):
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source [1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                                  delimiter = ',',
                                                                  unpack = True,
                                                                  converters = {0: bytesupdate2num('%Y-%m-%d')}
                                                                  )

    plt.plot_date(date, closep, '-', label = 'Price')

    plt.title('GRAPH PLOTTING FROM THE DATA GATHERED FROM THE INTERNET')
    plt.xlabel('DATE')
    plt.ylabel('PRICE')
    plt.legend()
    plt.show()

graph_data('TSLA')
