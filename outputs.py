import logging
from pathlib import Path

from docxtpl import DocxTemplate

from calc import enumerate_keys
from calc import merge_page_data
from calc import prepare_rows
from calc import split_to_page_size

WORD_OUTPUT_NAME = 'generated_labels'
OUTPUT_FOLDER = 'output'

log = logging.getLogger(__name__)


def to_console(data):
    """Print labels to console.

    Only for testing purposes.
    """
    from textwrap import dedent
    from string import Template

    log.info('outputting to console')

    template = Template(dedent("""
    ┌──────────────────────────────┐
    │${name_txt}│
    │                              │
    │${total_price_txt}│
    │                              │
    │${unit_txt}│
    └──────────────────────────────┘
    """))

    for item in data:
        total_price_label = f'{item["total_price"]},-'
        unit_label = f'1 {item["unit"]} = {item["unit_price"]} Kč'

        sub = {
            'name_txt'       : f'{item["name"]:^30}',
            'total_price_txt': f'{total_price_label:^30}',
            'unit_txt'       : f'{unit_label:^30}',
            }

        filled = template.substitute(sub)
        print(filled)


def to_word(data, template):
    """Output the label data to word files."""
    log.info('output to word started')

    # prepare output folder
    Path(OUTPUT_FOLDER).mkdir(exist_ok=True)

    # reformat the dicts for replace
    data = prepare_rows(data)

    # prepare paginated data
    page_splitted_data = split_to_page_size(data)

    # for each page
    for page_num, page_data in enumerate(page_splitted_data, start=1):
        # open new template for each page
        doc = DocxTemplate(template)

        # prepare the numbers for replacing
        replace_ready = enumerate_keys(page_data)
        context = merge_page_data(replace_ready)
        # make the replacement
        log.debug(f'replacing page {page_num}')
        doc.render(context=context)

        # save to new file
        filename = f'{page_num:02}_{WORD_OUTPUT_NAME}.docx'
        log.debug(f'saving to file {filename}')
        doc.save(Path(OUTPUT_FOLDER) / filename)

    log.info('output to word finished')
