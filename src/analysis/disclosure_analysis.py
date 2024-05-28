import pandas as pd
from datetime import timedelta
import os

from utils import display_utils, app_utils
from database import db_functions
from . import fetch_disclosure_dates as fetch_functions, static_analysis_utils, overall_results

def fetch_and_process_company_info():
    """
    Fetch and process the company information by displaying all companies, prompting for company ID, 
    and displaying the company info if available.
    """
    display_utils.display_all_companies()
    company_id = app_utils.prompt_company_id()
    
    if company_id == 0:
        print("Analysis cancelled due to invalid company ID.")
        return None, None

    company_info = db_functions.get_company_info(company_id)
    if company_info.empty:
        print(f"No company information available for Company ID: {company_id}.")
        return None, None
    
    display_utils.display_company_info(company_info)
    return company_id, company_info

def get_surrounding_stock_data(company_id, disclosure_date, window=7):
    """
    Fetch 7 days of stock market data before and after the disclosure date.
    """
    start_date = disclosure_date - timedelta(days=window)
    end_date = disclosure_date + timedelta(days=window)

    date_range = pd.date_range(start=start_date, end=end_date)
    date_strings = date_range.strftime('%Y-%m-%d').tolist()
    all_data = []

    for date_str in date_strings:
        data = db_functions.get_stock_data_with_disclosure_dates(company_id, pd.to_datetime(date_str))
        if not data.empty:
            all_data.append(data)

    combined_data = pd.concat(all_data, ignore_index=True)
    return combined_data

def display_surrounding_data(disclosure_date, surrounding_data):
    """
    Display the surrounding stock data for the given disclosure date.
    """
    print(f"\nSurrounding stock data for disclosure date: {disclosure_date}")
    display_utils.display_dataframe_to_user(f"Surrounding Data for {disclosure_date}", surrounding_data)

def collect_test_results(company_id, disclosure_date, surrounding_data):
    """
    Perform statistical tests and collect results.
    """
    test_results = static_analysis_utils.perform_t_test_analysis(company_id, disclosure_date, surrounding_data)
    return {
        'disclosure_date': disclosure_date,
        't_test_stat': test_results['t_test']['t_statistic'],
        't_test_p_value': test_results['t_test']['p_value'],
        'wilcoxon_stat': test_results['wilcoxon']['wilcoxon_statistic'],
        'wilcoxon_p_value': test_results['wilcoxon']['p_value'],
        'correlation_coeff': test_results['correlation']['correlation_coefficient'],
        'correlation_p_value': test_results['correlation']['p_value'],
        'mwu_stat': test_results['mannwhitneyu']['mwu_statistic'],
        'mwu_p_value': test_results['mannwhitneyu']['p_value']
    }

def perform_analysis(company_id, dates, availability):
    """
    Perform the full analysis for the given company and disclosure dates.
    """
    disclosure_stock_data = fetch_functions.retrieve_stock_data(company_id, dates, availability)
    display_utils.display_stock_data(company_id, disclosure_stock_data)

    analysis_results = []

    for _, row in disclosure_stock_data.iterrows():
        disclosure_date = row['Date']
        surrounding_data = get_surrounding_stock_data(company_id, pd.to_datetime(disclosure_date))
        display_surrounding_data(disclosure_date, surrounding_data)
        test_results = collect_test_results(company_id, disclosure_date, surrounding_data)
        
        # Collect surrounding stock data and test results
        analysis_results.append({
            'disclosure_date': disclosure_date,
            'surrounding_data': surrounding_data,
            'test_results': test_results
        })

    # Print the collected analysis results
    print("\nCollected Analysis Results:")
    for result in analysis_results:
        print(result['test_results'])

    # Analyze and display results using overall_results module
    overall_results.analyze_results([result['test_results'] for result in analysis_results])

    # Export results to Excel
    export_results_to_excel(analysis_results, company_id)

    return analysis_results

def export_results_to_excel(analysis_results, company_id):
    """
    Export analysis results to an Excel file with each element in a separate sheet.
    """
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    results_file = os.path.join(output_dir, f"analysis_results_company_{company_id}.xlsx")
    with pd.ExcelWriter(results_file, engine='xlsxwriter') as writer:
        for result in analysis_results:
            disclosure_date = result['disclosure_date']
            surrounding_data = result['surrounding_data']
            test_results_df = pd.DataFrame([result['test_results']])
            
            # Write surrounding data to a sheet
            surrounding_data.to_excel(writer, sheet_name=f"Data_{disclosure_date}", index=False)
            # Write test results to another sheet
            test_results_df.to_excel(writer, sheet_name=f"Results_{disclosure_date}", index=False)

    print(f"\nAnalysis results exported to {results_file}")

def stock_analysis_main():
    """
    Main function to run the stock analysis.
    """
    try:
        company_id, company_info = fetch_and_process_company_info()
        if company_id is None:
            return

        dates = fetch_functions.get_disclosure_dates(company_id)
        if not dates:
            print("No disclosure dates found.")
            return

        availability = fetch_functions.check_stock_data_availability(company_id, dates)
        if not availability:
            print(f"No stock data available for Company ID: {company_id}")
            return

        perform_analysis(company_id, dates, availability)

    except Exception as e:
        print(f"An error occurred during stock analysis: {e}")

