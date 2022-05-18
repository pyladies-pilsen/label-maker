from config import setup_logging

setup_logging()
import logging

from calc import calculate_unit_price
from inputs import csv_input
from outputs import to_console

log = logging.getLogger(__name__)


def main():
    logging.info('Start programu')
    data = csv_input()
    calculated_data = calculate_unit_price(data)
    to_console(calculated_data)


if __name__ == '__main__':
    main()
