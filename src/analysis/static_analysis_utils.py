# static_analysis_utils.py

from scipy.stats import ttest_rel, wilcoxon, pearsonr, mannwhitneyu

# Custom Modules
from . import plot_data, StockAnalysisResults
from utils import app_utils

def prepare_data(surrounding_data):
    """
    Prepare and clean the data for analysis.
    """
    surrounding_data['Stock Volume'] = surrounding_data['Stock Volume'].apply(app_utils.convert_volume)
    surrounding_data['Dow Jones Volume'] = surrounding_data['Dow Jones Volume'].apply(app_utils.convert_volume)

    try:
        surrounding_data = surrounding_data.astype({
            'Stock Open': 'float',
            'Stock Close': 'float',
            'Stock Volume': 'float',
            'Dow Jones Open': 'float',
            'Dow Jones Close': 'float',
            'Dow Jones Volume': 'float'
        })
    except ValueError as e:
        raise ValueError(f"Error in converting data types: {e}")

    surrounding_data['Stock Price Change'] = surrounding_data['Stock Close'] - surrounding_data['Stock Open']
    surrounding_data['Dow Jones Change'] = surrounding_data['Dow Jones Close'] - surrounding_data['Dow Jones Open']

    surrounding_data = surrounding_data.dropna()

    return surrounding_data

def perform_t_test(stock_changes, dow_jones_changes):
    """
    Perform a paired t-test.
    """
    try:
        t_stat, p_value = ttest_rel(stock_changes, dow_jones_changes)
        return t_stat, p_value
    except ValueError as e:
        raise ValueError(f"Error performing t-test: {e}")

def perform_wilcoxon_test(stock_changes, dow_jones_changes):
    """
    Perform Wilcoxon signed-rank test.
    """
    try:
        wilcoxon_stat, wilcoxon_p_value = wilcoxon(stock_changes, dow_jones_changes)
        return wilcoxon_stat, wilcoxon_p_value
    except ValueError as e:
        raise ValueError(f"Error performing Wilcoxon signed-rank test: {e}")

def perform_correlation_test(stock_changes, dow_jones_changes):
    """
    Perform Pearson correlation test.
    """
    try:
        correlation, corr_p_value = pearsonr(stock_changes, dow_jones_changes)
        return correlation, corr_p_value
    except ValueError as e:
        raise ValueError(f"Error calculating correlation: {e}")

def perform_mannwhitneyu_test(stock_changes, dow_jones_changes):
    """
    Perform Mann-Whitney U test.
    """
    try:
        mwu_stat, mwu_p_value = mannwhitneyu(stock_changes, dow_jones_changes)
        return mwu_stat, mwu_p_value
    except ValueError as e:
        raise ValueError(f"Error performing Mann-Whitney U test: {e}")

def perform_statistical_tests(surrounding_data):
    """
    Perform all statistical tests on the prepared data.
    """
    results = {}

    stock_changes = surrounding_data['Stock Price Change']
    dow_jones_changes = surrounding_data['Dow Jones Change']

    try:
        t_stat, p_value = perform_t_test(stock_changes, dow_jones_changes)
        results['t_test'] = {'t_statistic': t_stat, 'p_value': p_value}
    except ValueError as e:
        results['t_test'] = {'error': str(e)}

    try:
        wilcoxon_stat, wilcoxon_p_value = perform_wilcoxon_test(stock_changes, dow_jones_changes)
        results['wilcoxon'] = {'wilcoxon_statistic': wilcoxon_stat, 'p_value': wilcoxon_p_value}
    except ValueError as e:
        results['wilcoxon'] = {'error': str(e)}

    try:
        correlation, corr_p_value = perform_correlation_test(stock_changes, dow_jones_changes)
        results['correlation'] = {'correlation_coefficient': correlation, 'p_value': corr_p_value}
    except ValueError as e:
        results['correlation'] = {'error': str(e)}

    try:
        mwu_stat, mwu_p_value = perform_mannwhitneyu_test(stock_changes, dow_jones_changes)
        results['mannwhitneyu'] = {'mwu_statistic': mwu_stat, 'p_value': mwu_p_value}
    except ValueError as e:
        results['mannwhitneyu'] = {'error': str(e)}

    return results

def additional_insights(surrounding_data):
    """
    Generate additional insights from the data.
    """
    insights = {
        'stock_price_volatility': surrounding_data['Stock Price Change'].std(),
        'dow_jones_volatility': surrounding_data['Dow Jones Change'].std(),
        'average_stock_volume': surrounding_data['Stock Volume'].mean(),
        'average_dow_jones_volume': surrounding_data['Dow Jones Volume'].mean()
    }

    return insights

def summarize_findings(insights, surrounding_data):
    """
    Summarize the findings of the analysis.
    """
    summary = {
        'stock_price_change_mean': surrounding_data['Stock Price Change'].mean(),
        'dow_jones_change_mean': surrounding_data['Dow Jones Change'].mean(),
        'stock_volume_mean': insights['average_stock_volume'],
        'dow_jones_volume_mean': insights['average_dow_jones_volume'],
        'stock_price_volatility': insights['stock_price_volatility'],
        'dow_jones_volatility': insights['dow_jones_volatility']
    }

    return summary

def perform_t_test_analysis(company_id, disclosure_date, surrounding_data):
    """
    Perform comprehensive statistical analysis on stock data surrounding disclosure dates.
    """
    print(f"\nPerforming t-test analysis for disclosure date: {disclosure_date}")
    plotData = False
    resultsSummary = False

    results = StockAnalysisResults.StockAnalysisResults(company_id)

    try:
        surrounding_data = prepare_data(surrounding_data)
    except ValueError as e:
        print(e)
        return

    try:
        statistical_results = perform_statistical_tests(surrounding_data)
    except ValueError as e:
        print(e)
        return

    t_test_significant = statistical_results['t_test']['p_value'] < 0.05 if 'p_value' in statistical_results['t_test'] else False
    wilcoxon_significant = statistical_results['wilcoxon']['p_value'] < 0.05 if 'p_value' in statistical_results['wilcoxon'] else False
    correlation_significant = statistical_results['correlation']['p_value'] < 0.05 if 'p_value' in statistical_results['correlation'] else False
    mwu_significant = statistical_results['mannwhitneyu']['p_value'] < 0.05 if 'p_value' in statistical_results['mannwhitneyu'] else False

    results.set_t_test_results(
        statistical_results['t_test'].get('t_statistic', 0),
        statistical_results['t_test'].get('p_value', 1),
        t_test_significant,
        "The t-test result is statistically significant, indicating a significant difference between stock price change and Dow Jones change."
        if t_test_significant else "The t-test result is not statistically significant, indicating no significant difference between stock price change and Dow Jones change."
    )

    results.set_wilcoxon_results(
        statistical_results['wilcoxon'].get('wilcoxon_statistic', 0),
        statistical_results['wilcoxon'].get('p_value', 1),
        wilcoxon_significant,
        "The Wilcoxon test result is statistically significant, indicating a significant difference between stock price change and Dow Jones change."
        if wilcoxon_significant else "The Wilcoxon test result is not statistically significant, indicating no significant difference between stock price change and Dow Jones change."
    )

    results.set_correlation_results(
        statistical_results['correlation'].get('correlation_coefficient', 0),
        statistical_results['correlation'].get('p_value', 1),
        correlation_significant,
        f"The correlation is statistically significant, indicating a {'positive' if statistical_results['correlation'].get('correlation_coefficient', 0) > 0 else 'negative'} relationship between stock price change and Dow Jones change."
        if correlation_significant else "The correlation is not statistically significant, indicating no significant linear relationship between stock price change and Dow Jones change."
    )

    results.set_additional_insights(
        statistical_results['mannwhitneyu'].get('mwu_statistic', 0),
        statistical_results['mannwhitneyu'].get('p_value', 1),
        mwu_significant,
        "The Mann-Whitney U test result is statistically significant, indicating a significant difference between stock price change and Dow Jones change."
        if mwu_significant else "The Mann-Whitney U test result is not statistically significant, indicating no significant difference between stock price change and Dow Jones change."
    )

    insights = additional_insights(surrounding_data)
    summary = summarize_findings(insights, surrounding_data)

    results.set_additional_insights(
        insights['stock_price_volatility'], 
        insights['dow_jones_volatility'], 
        insights['average_stock_volume'], 
        insights['average_dow_jones_volume']
    )

    if resultsSummary:
        print("\nSummary of Findings:")
        results.set_summary(
            summary['stock_price_change_mean'], 
            summary['dow_jones_change_mean'], 
            summary['stock_volume_mean'], 
            summary['dow_jones_volume_mean'], 
            summary['stock_price_volatility'], 
            summary['dow_jones_volatility']
        )

    results.display_results()

    if plotData:
        plot_data.plot_time_series(surrounding_data, company_id)
        plot_data.plot_histograms(surrounding_data)
        plot_data.plot_correlation_matrix(surrounding_data)

    return statistical_results
