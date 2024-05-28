import numpy as np

def interpret_statistical_significance(p_value, alpha=0.05):
    return "Statistically significant" if p_value < alpha else "Not statistically significant"

def summarize_results(results):
    summary = {
        'total_disclosures': len(results),
        'significant_t_tests': sum(1 for r in results if r['t_test_p_value'] < 0.05),
        'significant_wilcoxon_tests': sum(1 for r in results if r['wilcoxon_p_value'] < 0.05),
        'significant_correlations': sum(1 for r in results if r['correlation_p_value'] < 0.05),
        'significant_mwu_tests': sum(1 for r in results if r['mwu_p_value'] < 0.05),
        'average_t_test_stat': np.mean([r['t_test_stat'] for r in results]),
        'average_wilcoxon_stat': np.mean([r['wilcoxon_stat'] for r in results]),
        'average_correlation_coeff': np.mean([r['correlation_coeff'] for r in results]),
        'average_mwu_stat': np.mean([r['mwu_stat'] for r in results])
    }
    return summary

def interpret_results(results):
    summary = summarize_results(results)
    
    interpretations = []
    for result in results:
        interpretations.append({
            'disclosure_date': result['disclosure_date'],
            't_test': interpret_statistical_significance(result['t_test_p_value']),
            'wilcoxon': interpret_statistical_significance(result['wilcoxon_p_value']),
            'correlation': interpret_statistical_significance(result['correlation_p_value']),
            'mwu': interpret_statistical_significance(result['mwu_p_value']),
            'correlation_coeff_interpretation': "Positive" if result['correlation_coeff'] > 0 else "Negative"
        })
    
    return summary, interpretations

def display_interpretations(summary, interpretations):
    print("\nSummary of Analysis Results:")
    print(f"Total disclosures analyzed: {summary['total_disclosures']}")
    print(f"Significant t-tests: {summary['significant_t_tests']} / {summary['total_disclosures']}")
    print(f"Significant Wilcoxon tests: {summary['significant_wilcoxon_tests']} / {summary['total_disclosures']}")
    print(f"Significant correlations: {summary['significant_correlations']} / {summary['total_disclosures']}")
    print(f"Significant Mann-Whitney U tests: {summary['significant_mwu_tests']} / {summary['total_disclosures']}")
    print(f"Average t-test statistic: {summary['average_t_test_stat']:.4f}")
    print(f"Average Wilcoxon statistic: {summary['average_wilcoxon_stat']:.4f}")
    print(f"Average correlation coefficient: {summary['average_correlation_coeff']:.4f}")
    print(f"Average Mann-Whitney U statistic: {summary['average_mwu_stat']:.4f}")
    
    print("\nDetailed Interpretations:")
    for interpretation in interpretations:
        print(f"\nDisclosure Date: {interpretation['disclosure_date']}")
        print(f"T-test: {interpretation['t_test']}")
        print(f"Wilcoxon: {interpretation['wilcoxon']}")
        print(f"Correlation: {interpretation['correlation']} ({interpretation['correlation_coeff_interpretation']})")
        print(f"Mann-Whitney U: {interpretation['mwu']}")
