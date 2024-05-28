import matplotlib.pyplot as plt

def plot_histograms(data):
    """
    Plot histograms for stock price changes and Dow Jones changes.
    """
    plt.figure(figsize=(14, 7))
    plt.subplot(1, 2, 1)
    plt.hist(data['Stock Price Change'], bins=30, alpha=0.7, label='Stock Price Change')
    plt.xlabel('Stock Price Change')
    plt.title('Distribution of Stock Price Changes')

    plt.subplot(1, 2, 2)
    plt.hist(data['Dow Jones Change'], bins=30, alpha=0.7, label='Dow Jones Change', color='orange')
    plt.xlabel('Dow Jones Change')
    plt.title('Distribution of Dow Jones Changes')
    plt.tight_layout()
    plt.show()
