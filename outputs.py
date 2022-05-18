import logging

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
