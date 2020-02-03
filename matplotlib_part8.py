import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

def test1():

    plt.style.use('seaborn')

    dates = [datetime(2019, 5, i) for i in range(24,31)]

    y = [0, 1, 3, 4, 6, 5, 7]

    plt.plot_date(dates, y, linestyle='solid')

    # plt.gcf = get current figure
    plt.gcf().autofmt_xdate()

    date_format = mpl_dates.DateFormatter('%b, %d %Y')
    # plt.gca = get current axis
    plt.gca().xaxis.set_major_formatter(date_format)

    plt.tight_layout()
    plt.show()

def test2():

    plt.style.use('seaborn')

    data = pd.read_csv('test_files/bitcoin_prices.csv')

    data['Date'] = pd.to_datetime(data['Date'])
    data.sort_values('Date', inplace=True)

    price_dates = data['Date']
    price_close = data['Close']

    plt.plot_date(price_dates, price_close, linestyle='solid')

    # plt.gcf = get current figure
    plt.gcf().autofmt_xdate()

    plt.title('Bitcoin Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    test2()