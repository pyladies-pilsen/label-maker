import logging
from functools import reduce
from itertools import zip_longest
from operator import or_

LABELS_PER_PAGE = 36

log = logging.getLogger(__name__)


def calculate_unit_price(data):
    """Calculate price per unit."""
    log.debug('claculating unit price')
    for item in data:
        item['unit_price'] = round(item['total_price'] / item['quantity'], 2)
    log.debug('done')
    return data


def split_to_page_size(data):
    """split data to chunks based on labels per page"""
    log.debug('splitting data to pages')
    # prepare fill dict with empty values
    # NOTE: this is so the rest of the page fills as blank and is not printed
    fill_value = {k: '' for k in data[0]}
    args = [iter(data)] * LABELS_PER_PAGE
    log.debug('done')
    return zip_longest(*args, fillvalue=fill_value)


def enumerate_keys(page_data):
    """Edit keys so they can be used in replacement.

    name -> name_1, name_2 ...
    """
    log.debug('enumerating keys')
    result = []
    for num, item in enumerate(page_data, start=1):
        renamed = {}
        for key, value in item.items():
            renamed[f'{key}_{num}'] = value
        result.append(renamed)
    log.debug('done')
    return result


def merge_page_data(data):
    """Merge list of dictionaries into one."""
    log.debug('merging page data to a single dictionary')
    data = reduce(or_, data)
    log.debug('done')
    return data


def round_all_values(dictionary):
    """Round all numeric values in a dictionary."""
    log.debug('rounding numeric values')
    new_dict = {}
    for k, v in dictionary.items():
        if k == 'unit_price':
            new_dict[k] = v
            continue
        try:
            new_dict[k] = int(round(v, 0))
        except TypeError:
            new_dict[k] = v
    log.debug('done')
    return new_dict


def prepare_rows(data):
    """Reformat the dicts for replacing.

    We need keys "top_row" "price" "bottom_row"
    """
    log.debug('preparing rows')
    new_data = []
    for dct in data:
        dct = round_all_values(dct)
        top_row = '{name} {form} {quantity} {unit}'.format(**dct)
        price = '{total_price},-'.format(**dct)
        bottom_row = '1 {unit} = {unit_price} Kč'.format(**dct)
        new_data.append(
            {
                'top_row'   : top_row,
                'price'     : price,
                'bottom_row': bottom_row,
                }
            )
    log.debug('done')
    return new_data
