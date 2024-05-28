import matplotlib.pyplot as plt

def plot_significance(results):
    dates = [r['disclosure_date'] for r in results]
    t_test_p_values = [r['t_test_p_value'] for r in results]
    wilcoxon_p_values = [r['wilcoxon_p_value'] for r in results]
    correlation_p_values = [r['correlation_p_value'] for r in results]
    mwu_p_values = [r['mwu_p_value'] for r in results]

    plt.figure(figsize=(14, 10))

    plt.subplot(2, 2, 1)
    plt.plot(dates, t_test_p_values, marker='o', linestyle='-', label='T-test P-values')
    plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Level (0.05)')
    plt.xlabel('Disclosure Dates')
    plt.ylabel('P-values')
    plt.title('T-test P-values Over Time')
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(dates, wilcoxon_p_values, marker='o', linestyle='-', label='Wilcoxon P-values')
    plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Level (0.05)')
    plt.xlabel('Disclosure Dates')
    plt.ylabel('P-values')
    plt.title('Wilcoxon P-values Over Time')
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(dates, correlation_p_values, marker='o', linestyle='-', label='Correlation P-values')
    plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Level (0.05)')
    plt.xlabel('Disclosure Dates')
    plt.ylabel('P-values')
    plt.title('Correlation P-values Over Time')
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(dates, mwu_p_values, marker='o', linestyle='-', label='Mann-Whitney U P-values')
    plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Level (0.05)')
    plt.xlabel('Disclosure Dates')
    plt.ylabel('P-values')
    plt.title('Mann-Whitney U P-values Over Time')
    plt.legend()

    plt.tight_layout()
    plt.show()
