"""Inputs.

Take input and return data in format of list[dict]


Example of output:
[
    {
    'name': 'Bromhexin',
    'form': 'gtt'
    'unit': 'ml',
    'quantity': 100,
    'total_price': 194.0,
    },
    {
    'name': 'Bromhexin',
    'unit': 'ml',
    'quantity': 100,
    'total_price': 194.0,
    },
    {...},
    {...},
]

"""


def user_input():
    """Take input from user.

    Exmaple input:
        Nazev: Bromhexin
        Forma: gtt
        Jednotky: ml
        Pocet: 100
        Celkova cena: 194
        -- další? [a/n]:
    """

    entries = []
    while True:
        item = {
            'name'       : input('Název: '),
            'form'       : input('Forma: '),
            'unit'       : input('Jednotky: '),
            'quantity'   : input('Počet: '),
            'total_price': input('Celková cena [Kč]: '),
            }
        entries.append(item)

        next_q = input('-- další? [a/n]: ')
        if next_q == 'n':
            return entries
