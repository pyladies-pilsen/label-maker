from config import setup_logging

setup_logging()
import logging

from calc import calculate_unit_price
from inputs import user_input

log = logging.getLogger(__name__)


def main():
    logging.info('Start programu')
    data = user_input()
    calculated_data = calculate_unit_price(data)
    log.info(calculated_data)


if __name__ == '__main__':
    main()
