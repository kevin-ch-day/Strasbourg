import pandas as pd
from mysql.connector import Error
from datetime import datetime
from . import db_connection, db_utils

# Create an instance of the DatabaseConnection
db_instance = db_connection.DatabaseConnection()

def execute_query(sql, params=None):
    """
    Execute an SQL query and return the results in a DataFrame.
    """
    try:
        with db_instance.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params or ())
            result = cursor.fetchall()
            if result:
                columns = [desc[0] for desc in cursor.description]
                return pd.DataFrame(result, columns=columns)
            else:
                return pd.DataFrame()
    except Error as e:
        print(f"SQL execution error: {e}")
        return pd.DataFrame()

def get_data_breach_disclosures(company_id):
    """
    Fetch data breach disclosure dates for a given company.
    """
    sql = """
    SELECT DisclosureDate AS 'Disclosure Date'
    FROM data_breach_disclosures
    WHERE CompanyID = %s
    ORDER BY DisclosureDate ASC;
    """
    return execute_query(sql, (company_id,))

def get_company_info(company_id=None):
    """
    Fetch company information either for a specific company or all companies.
    """
    base_query = """
        SELECT CompanyID AS 'ID', CompanyName AS 'Name', Location AS 'Location', StockSymbol AS 'Stock Symbol'
        FROM company_info
    """
    if company_id:
        query = base_query + " WHERE CompanyID = %s ORDER BY CompanyID;"
        return execute_query(query, (company_id,))
    else:
        query = base_query + " ORDER BY CompanyID;"
        return execute_query(query)

def fetch_stock_and_dow_jones_data(company_id, dates):
    if not isinstance(dates, list):
        dates = [dates]

    results_dict = {}
    for date in dates:
        formatted_date = date.strftime('%Y-%m-%d')
        sql = f"""
            SELECT x.Date, COUNT(x.Date) > 0 AS HasStockData
            FROM stock_data x
            LEFT JOIN dow_jones y ON y.Date = x.Date
            WHERE x.CompanyID = {company_id} AND x.Date = '{formatted_date}'
            GROUP BY x.Date;
        """
        df = execute_query(sql)
        if df.empty:
            results_dict[formatted_date] = False
        else:
            has_data = df.iloc[0]['HasStockData']
            results_dict[formatted_date] = bool(has_data)

    return results_dict

def get_stock_data_with_disclosure_dates(company_id, disclosure_date):
    """
    Fetch detailed stock and Dow Jones data for a specific date, ensuring date handling is robust.
    """
    # Format the date for the query
    formatted_date = db_utils.format_date_for_query(disclosure_date)
    if formatted_date is None:
        print(f"Invalid date format for: {disclosure_date}")
        return pd.DataFrame(columns=['Date', 'Stock Open', 'Stock Close', 'Stock Volume',
                                     'Dow Jones Open', 'Dow Jones Close', 'Dow Jones Volume'])

    query = f"""
        SELECT x.Date,
            x.Open AS 'Stock Open',
            x.Close AS 'Stock Close',
            x.Volume AS 'Stock Volume',
            y.Open AS 'Dow Jones Open',
            y.Close AS 'Dow Jones Close',
            y.Volume AS 'Dow Jones Volume'
        FROM stock_data x
        JOIN dow_jones y ON y.Date = x.Date
        WHERE x.CompanyID = {company_id} AND x.Date = {formatted_date}
        ORDER BY x.Date;
    """
    
    results = execute_query(query)
    return results
