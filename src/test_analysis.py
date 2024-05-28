# main.py

from analysis import disclosure_analysis
from utils import setup_logging

logger = setup_logging.setup_logger('app', log_file='app.log')

def main():
    logger.info("Starting Strasbourg")
    disclosure_analysis.stock_analysis_main()

if __name__ == "__main__":
    main()
