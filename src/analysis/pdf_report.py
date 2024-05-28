import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image, Spacer
from reportlab.lib.units import inch
from reportlab.lib import colors
import matplotlib.pyplot as plt
from . import plot_data

def save_results_to_pdf(summary, interpretations, results, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    elements = []
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=1))
    
    # Title
    title = Paragraph("Statistical Analysis Report", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))
    
    # Summary Section
    summary_title = Paragraph("Summary of Analysis Results", styles['Heading2'])
    elements.append(summary_title)
    elements.append(Spacer(1, 12))
    
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
    summary_table = Table(summary_data, hAlign='LEFT')
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
    elements.append(Spacer(1, 12))
    
    # Detailed Interpretations Section
    interpretations_title = Paragraph("Detailed Interpretations", styles['Heading2'])
    elements.append(interpretations_title)
    elements.append(Spacer(1, 12))
    
    for interpretation in interpretations:
        interpretation_paragraph = Paragraph(f"""
        <b>Disclosure Date:</b> {interpretation['disclosure_date']}<br/>
        <b>T-test:</b> {interpretation['t_test']}<br/>
        <b>Wilcoxon:</b> {interpretation['wilcoxon']}<br/>
        <b>Correlation:</b> {interpretation['correlation']} ({interpretation['correlation_coeff_interpretation']})<br/>
        <b>Mann-Whitney U:</b> {interpretation['mwu']}<br/>
        """, styles['Normal'])
        elements.append(interpretation_paragraph)
        elements.append(Spacer(1, 12))
    
    # Add significance plots
    plot_data.plot_significance(results)
    plt.savefig("significance_plot.png")
    elements.append(Paragraph("Significance Plots", styles['Heading2']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("The following plots show the p-values over time for different tests.", styles['Normal']))
    elements.append(Spacer(1, 12))
    elements.append(Image("significance_plot.png", width=6*inch, height=3*inch))
    
    doc.build(elements)

def analyze_results(results):
    from .interpretation_utils import interpret_results, display_interpretations

    summary, interpretations = interpret_results(results)
    display_interpretations(summary, interpretations)

    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "analysis_results.pdf")
    save_results_to_pdf(summary, interpretations, results, output_file)
    print(f"\nAnalysis results saved to {output_file}")
