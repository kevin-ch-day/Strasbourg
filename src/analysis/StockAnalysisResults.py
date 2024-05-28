from tabulate import tabulate

class StockAnalysisResults:
    def __init__(self, company_id):
        self.company_id = company_id
        self.t_test_results = None
        self.wilcoxon_results = None
        self.correlation_results = None
        self.additional_insights = None
        self.summary = None

    def set_t_test_results(self, t_stat, p_value, significant, interpretation):
        self.t_test_results = {
            't_statistic': t_stat,
            'p_value': p_value,
            'significant': significant,
            'interpretation': interpretation
        }

    def set_wilcoxon_results(self, wilcoxon_stat, wilcoxon_p_value, significant, interpretation):
        self.wilcoxon_results = {
            'wilcoxon_statistic': wilcoxon_stat,
            'p_value': wilcoxon_p_value,
            'significant': significant,
            'interpretation': interpretation
        }

    def set_correlation_results(self, correlation, corr_p_value, significant, interpretation):
        self.correlation_results = {
            'correlation_coefficient': correlation,
            'p_value': corr_p_value,
            'significant': significant,
            'interpretation': interpretation
        }

    def set_additional_insights(self, stock_price_volatility, dow_jones_volatility, avg_stock_volume, avg_dow_jones_volume):
        self.additional_insights = {
            'stock_price_volatility': stock_price_volatility,
            'dow_jones_volatility': dow_jones_volatility,
            'average_stock_volume': avg_stock_volume,
            'average_dow_jones_volume': avg_dow_jones_volume
        }

    def set_summary(self, stock_price_change_mean, dow_jones_change_mean, stock_volume_mean, dow_jones_volume_mean, stock_price_volatility, dow_jones_volatility):
        self.summary = {
            'stock_price_change_mean': stock_price_change_mean,
            'dow_jones_change_mean': dow_jones_change_mean,
            'stock_volume_mean': stock_volume_mean,
            'dow_jones_volume_mean': dow_jones_volume_mean,
            'stock_price_volatility': stock_price_volatility,
            'dow_jones_volatility': dow_jones_volatility
        }

    def display_t_test_results(self):
        print(f"\n T-test Results for Company ID: {self.company_id}")
        if self.t_test_results:
            t_test_table = [
                ["T-statistic", f"{self.t_test_results['t_statistic']:.4f}"],
                ["P-value", f"{self.t_test_results['p_value']:.4f}"],
                ["Significant", "Yes" if self.t_test_results['significant'] else "No"],
                ["Interpretation", self.t_test_results['interpretation']]
            ]
            print(tabulate(t_test_table, headers=["Metric", "Value"], tablefmt="grid"))

    def display_wilcoxon_results(self):
        print("\n Wilcoxon Signed-Rank Test Results:")
        if self.wilcoxon_results:
            wilcoxon_table = [
                ["Wilcoxon statistic", f"{self.wilcoxon_results['wilcoxon_statistic']:.4f}"],
                ["P-value", f"{self.wilcoxon_results['p_value']:.4f}"],
                ["Significant", "Yes" if self.wilcoxon_results['significant'] else "No"],
                ["Interpretation", self.wilcoxon_results['interpretation']]
            ]
            print(tabulate(wilcoxon_table, headers=["Metric", "Value"], tablefmt="grid"))

    def display_correlation_results(self):
        print("\n Correlation Analysis:")
        if self.correlation_results:
            correlation_table = [
                ["Correlation coefficient", f"{self.correlation_results['correlation_coefficient']:.4f}"],
                ["P-value", f"{self.correlation_results['p_value']:.4f}"],
                ["Significant", "Yes" if self.correlation_results['significant'] else "No"],
                ["Interpretation", self.correlation_results['interpretation']]
            ]
            print(tabulate(correlation_table, headers=["Metric", "Value"], tablefmt="grid"))

    def display_additional_insights(self):
        print("\n Additional Insights:")
        if self.additional_insights:
            insights_table = [
                ["Stock Price Volatility (Standard Deviation)", f"{self.additional_insights['stock_price_volatility']:.4f}"],
                ["Dow Jones Volatility (Standard Deviation)", f"{self.additional_insights['dow_jones_volatility']:.4f}"],
                ["Average Stock Volume", f"{self.additional_insights['average_stock_volume']:.4f}"],
                ["Average Dow Jones Volume", f"{self.additional_insights['average_dow_jones_volume']:.4f}"]
            ]
            print(tabulate(insights_table, headers=["Metric", "Value"], tablefmt="grid"))

    def display_summary(self):
        if self.summary:
            summary_table = [
                ["Stock Price Change Mean", f"{self.summary['stock_price_change_mean']:.4f}"],
                ["Dow Jones Change Mean", f"{self.summary['dow_jones_change_mean']:.4f}"],
                ["Stock Volume Mean", f"{self.summary['stock_volume_mean']:.4f}"],
                ["Dow Jones Volume Mean", f"{self.summary['dow_jones_volume_mean']:.4f}"],
                ["Stock Price Volatility", f"{self.summary['stock_price_volatility']:.4f}"],
                ["Dow Jones Volatility", f"{self.summary['dow_jones_volatility']:.4f}"]
            ]
            print(tabulate(summary_table, headers=["Metric", "Value"], tablefmt="grid"))

    def display_results(self):
        self.display_t_test_results()
        self.display_wilcoxon_results()
        self.display_correlation_results()
        self.display_additional_insights()
        self.display_summary()
