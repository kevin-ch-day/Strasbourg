import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

from . import plot_data

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

def save_results_to_pdf(summary, interpretations, results, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    elements = []
    
    styles = getSampleStyleSheet()
    title = Paragraph("Statistical Analysis Report", styles['Title'])
    elements.append(title)

    # Summary Section
    summary_title = Paragraph("Summary of Analysis Results", styles['Heading2'])
    elements.append(summary_title)
    
    summary_data = [
        ["Total disclosures analyzed", summary['total_disclosures']],
        ["Significant t-tests", f"{summary['significant_t_tests']} / {summary['total_disclosures']}"],
        ["Significant Wilcoxon tests", f"{summary['significant_wilcoxon_tests']} / {summary['total_disclosures']}"],
        ["Significant correlations", f"{summary['significant_correlations']} / {summary['total_disclosures']}"],
        ["Significant Mann-Whitney U tests", f"{summary['significant_mwu_tests']} / {summary['total_disclosures']}"],
        ["Average t-test statistic", f"{summary['average_t_test_stat']:.4f}"],
        ["Average Wilcoxon statistic", f"{summary['average_wilcoxon_stat']:.4f}"],
        ["Average correlation coefficient", f"{summary['average_correlation_coeff']:.4f}"],
        ["Average Mann-Whitney U statistic", f"{summary['average_mwu_stat']:.4f}"]
    ]
    summary_table = Table(summary_data)
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(summary_table)
    
    # Detailed Interpretations Section
    interpretations_title = Paragraph("Detailed Interpretations", styles['Heading2'])
    elements.append(interpretations_title)
    
    for interpretation in interpretations:
        interpretation_paragraph = Paragraph(f"""
        <b>Disclosure Date:</b> {interpretation['disclosure_date']}<br/>
        <b>T-test:</b> {interpretation['t_test']}<br/>
        <b>Wilcoxon:</b> {interpretation['wilcoxon']}<br/>
        <b>Correlation:</b> {interpretation['correlation']} ({interpretation['correlation_coeff_interpretation']})<br/>
        <b>Mann-Whitney U:</b> {interpretation['mwu']}<br/>
        """, styles['Normal'])
        elements.append(interpretation_paragraph)
    
    # Add significance plots
    plot_data.plot_significance(results)
    plt.savefig("significance_plot.png")
    elements.append(Paragraph("Significance Plots", styles['Heading2']))
    elements.append(Paragraph("The following plots show the p-values over time for different tests.", styles['Normal']))
    elements.append(Paragraph("<img src='significance_plot.png' width='500' height='300'/>", styles['Normal']))

    doc.build(elements)

def analyze_results(results):
    summary, interpretations = interpret_results(results)
    display_interpretations(summary, interpretations)

    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "analysis_results.pdf")
    save_results_to_pdf(summary, interpretations, results, output_file)
    print(f"\nAnalysis results saved to {output_file}")

