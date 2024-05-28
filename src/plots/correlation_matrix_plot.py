import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_matrix(data):
    """
    Plot the correlation matrix for all variables.
    """
    corr_matrix = data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()
