# main.py

from datetime import datetime

import analysis
from utils import setup_logging, display_utils

logger = setup_logging.setup_logger('app', log_file='app.log')

def main():
    logger.info("Starting Strasbourg")
    greeting()
    
    while True:
        print("\nMain Menu:")
        print(" 1. Display company info")
        print(" 2. Analyze company data")
        print(" 0. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '0':
            logger.info("Exiting.")
            break

        elif choice == '1':
            display_utils.display_company_info()

        elif choice == '2':
            analysis.stock_analysis_main()
        
        else:
            print("Invalid choice. Please try again.")

def greeting():
    current_datetime = datetime.now().strftime("%m-%d-%Y %I:%M %p")
    print("*** Project: Strasbourg ***")
    print(f"{current_datetime}")

if __name__ == "__main__":
    main()
