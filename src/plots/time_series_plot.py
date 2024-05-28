import matplotlib.pyplot as plt

def plot_time_series(data, company_id):
    """
    Plot time series for stock prices and Dow Jones indices.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Stock Close'], label='Stock Close Price')
    plt.plot(data['Date'], data['Dow Jones Close'], label='Dow Jones Close Price', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(f'Time Series of Stock and Dow Jones Close Prices for Company ID: {company_id}')
    plt.legend()
    plt.show()
