# fetch_disclosure_dates.py

import pandas as pd
from datetime import timedelta
from database import db_functions

def get_disclosure_dates(company_id):
    dates = db_functions.get_data_breach_disclosures(company_id)
    if dates.empty:
        print(f"No disclosure dates found for Company ID {company_id}.")
        return []
    return pd.to_datetime(dates['Disclosure Date']).tolist()

def check_stock_data_availability(company_id, dates):
    availability = db_functions.fetch_stock_and_dow_jones_data(company_id, dates)
    print("\nStock data availability for each date:")
    for date, available in availability.items():
        print(f"Date: {date}; Stock Data Available: {'Yes' if available else 'No'}")
    return availability

def find_next_available_date(company_id, start_date, max_days=7):
    print(f"\nSearching for next available date from: {start_date.strftime('%Y-%m-%d')}")
    for day in range(1, max_days + 1):
        next_date = start_date + timedelta(days=day)
        next_date_str = next_date.strftime('%Y-%m-%d')
        print(f"Checking date: {next_date_str}")
        data = db_functions.get_stock_data_with_disclosure_dates(company_id, next_date)
        if not data.empty:
            return next_date
    print(f"\nNo available date found within {max_days} days after {start_date.strftime('%Y-%m-%d')}")
    return None

def retrieve_stock_data(company_id, dates, availability):
    stock_data = []
    print()
    for date in dates:
        date_str = date.strftime('%Y-%m-%d')
        if date_str in availability and availability[date_str]:
            print(f"Fetching stock data for date: {date_str}")
            data = db_functions.get_stock_data_with_disclosure_dates(company_id, date)
            stock_data.append(data)
        else:
            print(f"No stock data available for date: {date_str}")
            next_available_date = find_next_available_date(company_id, date)
            if next_available_date:
                next_date_str = next_available_date.strftime('%Y-%m-%d')
                print(f"Next available date: {next_date_str}")
                data = db_functions.get_stock_data_with_disclosure_dates(company_id, next_available_date)
                stock_data.append(data)
            else:
                print(f"No stock data available within 7 days after {date_str}")
    
    combined_stock_data = pd.concat(stock_data, ignore_index=True)
    return combined_stock_data
