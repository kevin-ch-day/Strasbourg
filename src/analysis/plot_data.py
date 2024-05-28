# plot_data.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(data, company_id):
    """
    Plot time series for stock prices and Dow Jones indices.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Stock Close'], label='Stock Close Price', color='blue')
    plt.plot(data['Date'], data['Dow Jones Close'], label='Dow Jones Close Price', linestyle='--', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(f'Time Series of Stock and Dow Jones Close Prices for Company ID: {company_id}')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_histograms(data):
    """
    Plot histograms for stock price changes and Dow Jones changes.
    """
    plt.figure(figsize=(14, 7))
    
    plt.subplot(1, 2, 1)
    sns.histplot(data['Stock Price Change'], bins=30, kde=True, color='blue')
    plt.xlabel('Stock Price Change')
    plt.title('Distribution of Stock Price Changes')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    sns.histplot(data['Dow Jones Change'], bins=30, kde=True, color='orange')
    plt.xlabel('Dow Jones Change')
    plt.title('Distribution of Dow Jones Changes')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def plot_correlation_matrix(data):
    """
    Plot the correlation matrix for all variables.
    """
    corr_matrix = data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

def plot_significance(results):
    dates = [r['disclosure_date'] for r in results]
    t_test_p_values = [r['t_test_p_value'] for r in results]
    wilcoxon_p_values = [r['wilcoxon_p_value'] for r in results]
    correlation_p_values = [r['correlation_p_value'] for r in results]
    mwu_p_values = [r['mwu_p_value'] for r in results]

    plt.figure(figsize=(14, 10))

    plt.subplot(2, 2, 1)
    plt.plot(dates, t_test_p_values, marker='o', linestyle='-', label='T-test P-values', color='blue')
    plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Level (0.05)')
    plt.xlabel('Disclosure Dates')
    plt.ylabel('P-values')
    plt.title('T-test P-values Over Time')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.plot(dates, wilcoxon_p_values, marker='o', linestyle='-', label='Wilcoxon P-values', color='green')
    plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Level (0.05)')
    plt.xlabel('Disclosure Dates')
    plt.ylabel('P-values')
    plt.title('Wilcoxon P-values Over Time')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.plot(dates, correlation_p_values, marker='o', linestyle='-', label='Correlation P-values', color='purple')
    plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Level (0.05)')
    plt.xlabel('Disclosure Dates')
    plt.ylabel('P-values')
    plt.title('Correlation P-values Over Time')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.plot(dates, mwu_p_values, marker='o', linestyle='-', label='Mann-Whitney U P-values', color='orange')
    plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Level (0.05)')
    plt.xlabel('Disclosure Dates')
    plt.ylabel('P-values')
    plt.title('Mann-Whitney U P-values Over Time')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
