from datetime import datetime

def parse_date(date_str):
    """
    Convert a string to a datetime object.
    """
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print(f"Invalid date format: {date_str}")
        return None

def format_date_for_query(date):
    """
    Format a datetime object or a date string for SQL query.
    """
    if isinstance(date, datetime):
        return f"'{date.strftime('%Y-%m-%d')}'"
    elif isinstance(date, str):
        date_obj = parse_date(date)
        if date_obj:
            return f"'{date_obj.strftime('%Y-%m-%d')}'"
        else:
            return None
    else:
        print(f"Unrecognized date type: {date}")
        return None
