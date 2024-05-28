from database import db_functions
import pandas as pd
from tabulate import tabulate

def display_dataframe_to_user(title, df):
    try:
        print("\n" + title)
        print("=" * len(title))
        
        if df.empty:
            print("The DataFrame is empty.")
            return

        table = tabulate(df, headers='keys', tablefmt='psql')
        print(table)

    except Exception as e:
        print(f"Error displaying DataFrame: {e}")

def display_all_companies():
    company_info_df = db_functions.get_company_info()
    if company_info_df.empty:
        print("No company information available.")
    else:
        print("\n** Company Information **")
        
        # Remove 'Inc.' from the 'Name' column
        company_info_df['Name'] = company_info_df['Name'].str.replace(', Inc.', '')
        
        # Format the output for better display
        formatted_df = company_info_df.copy()
        formatted_df['Name'] = formatted_df['Name'].str.ljust(30)
        formatted_df['Stock Symbol'] = formatted_df['Stock Symbol'].str.ljust(10)
        
        # Print headers
        headers = ['ID', 'Name', 'Stock Symbol']
        header_str = ' | '.join(headers)
        print(header_str)
        print('-' * len(header_str))
        
        # Display the formatted DataFrame
        for _, row in formatted_df.iterrows():
            print(f"{row['ID']:2} | {row['Name']} | {row['Stock Symbol']}")

def display_disclosure_dates_count(disclosure_dates):
    # Display the number of disclosure dates for the given company ID.
    line = "=" * 40
    print(f"\n{line}")
    print(f"   Disclosure Dates: {len(disclosure_dates)}")
    print(f"{line}")
    for index, date in enumerate(disclosure_dates, start=1):
        formatted_date = date.strftime("%m-%d-%Y  %A")
        print(f" [{index}] {formatted_date}")

def display_company_info(company_info):
    if company_info.empty:
        print("No company information available.")
        return
    
    row = company_info.iloc[0]
    line = "=" * 40
    print(f"\n{line}")
    print("   Company Information")
    print(f"{line}")
    print(f" ID: {row['ID']}")
    print(f" Name: {row['Name']}")
    print(f" Location: {row['Location']}")
    print(f" Stock Symbol: {row['Stock Symbol']}")

def display_stock_data(company_id, stock_data_df):
    print(f"\nCompany ID: {company_id} Stock Data")
    if not stock_data_df.empty:
        print(tabulate(stock_data_df, headers='keys', tablefmt='grid'))
    else:
        print("No data available.")
