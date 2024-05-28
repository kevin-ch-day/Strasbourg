# app_utils.py

import pandas as pd
from database import db_functions

def format_stock_data_df(df):
    try:
        if 'Date' not in df.columns:
            raise ValueError("Input DataFrame must contain 'Date' column")

        expected_columns = ['Date', 'Stock Open', 'Stock Close', 'Stock Volume', 'Dow Jones Open', 'Dow Jones Close', 'Dow Jones Volume']
        if not all(col in df.columns for col in expected_columns):
            raise ValueError(f"Input DataFrame must contain columns: {expected_columns}")

        df['Date'] = pd.to_datetime(df['Date']).dt.date
        df['Stock Open'] = pd.to_numeric(df['Stock Open'], errors='coerce')
        df['Stock Close'] = pd.to_numeric(df['Stock Close'], errors='coerce')
        df['Stock Volume'] = pd.to_numeric(df['Stock Volume'], errors='coerce')
        df['Dow Jones Open'] = pd.to_numeric(df['Dow Jones Open'], errors='coerce')
        df['Dow Jones Close'] = pd.to_numeric(df['Dow Jones Close'], errors='coerce')
        df['Dow Jones Volume'] = pd.to_numeric(df['Dow Jones Volume'].str.replace('M', '').astype(float) * 1e6, errors='coerce')

        df = df.dropna()

        print("Formatted DataFrame:")
        print(df.head())
        return df
    
    except Exception as e:
        print(f"Error in format_stock_data_df: {e}")
        return df

def prompt_company_id():
    """Prompt the user for a company ID."""
    while True:
        company_id_input = input("\nEnter a company ID to analyze (0 to cancel): ")
        if company_id_input == '0':
            return 0
        
        try:
            company_id = int(company_id_input)
            if company_id < 0:
                raise ValueError("Company ID must be a positive integer.")
            return company_id
        except ValueError as e:
            print(f"Error: {e}")

def get_disclosure_dates(company_id):
    """
    Retrieve data breach disclosure dates for a specific company.
    Requires the company ID and returns a list of disclosure dates.
    """
    df_disclosures = db_functions.get_data_breach_disclosures(company_id)
    if df_disclosures.empty:
        return []

    disclosure_dates = df_disclosures['Disclosure Date'].tolist()
    
    try:
        return pd.to_datetime(disclosure_dates).tolist()
    except Exception as e:
        print(f"Error converting disclosure dates to datetime: {e}")
        return []
    
def convert_volume(volume_str):
    """
    Convert volume strings with suffixes 'M' (million) and 'B' (billion) to float.
    """
    if isinstance(volume_str, str):
        if 'M' in volume_str:
            return float(volume_str.replace('M', '')) * 1e6
        elif 'B' in volume_str:
            return float(volume_str.replace('B', '')) * 1e9
    return float(volume_str)