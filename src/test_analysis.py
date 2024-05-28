# main.py

from analysis import analyze_results
from utils import setup_logging

logger = setup_logging.setup_logger('app', log_file='app.log')

def main():
    logger.info("Starting Strasbourg")
    analyze_results.stock_analysis_main()

if __name__ == "__main__":
    main()
