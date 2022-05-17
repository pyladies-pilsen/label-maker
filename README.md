# Label maker - tvorba cenovek

> Tento projek je součástí navazujícího kurzu [pyladies Plzeň](https://pyladies.cz/plzen/).

## Popis projektu

Program, který usnadňuje práci při tvorbě cenovek v lékárně.

Uživatel zadá potřebné hodnoty, výsupem je pak tisknutelný soubor připravený k rozstříhání.

![ilustracni_foto_cedulky](resources/vyplnena.jpg)

---

## Vstupy:

### Z příkazové řádky pomocí inputů

```commandline
python label_maker.py --uzivatel
Nazev: Bromhexin
Forma: gtt
Jednotky: ml
Pocet: 100
Celkova cena: 194
další? [a/n]: 
```

### Ze souboru (csv)

```commandline
python label_maker.py --soubor cedulky.csv
```

### Pomocí commandline agrumentů

```commandline
python label_maker.py --nazev Bromhexin --jednotka ml --mnozstvi 100 --cena 194
```

### Omezení vstupu jednotlivých polí

#### Nazev:

- max 60 znaků (doladit, možno i dvouřádkový)

#### Celková cena:

- musí umožnit 4 cifry `1200,-`

#### Jednotky:

- pouze jedna z možností (ml, kus, tbl, gtt ...)

#### Počet:

- vždy celé číslo (int)

#### Jednotková cena:

- zaokrouhlit na 2 des.m. `12.54,-`

---

## Výstupy

- soubor s cedulkami připravený pro tisk.
- seznam vygenerovaných cedulek.
- csv soubor který je možnost programem načíst

---

## Pro programátory:

### tvar dat za vstupem

Vstupní metody vrací výstup ve tvaru list slovníků.  
Např.:

```python
data = [
    {
        'name'       : 'Bromhexin',
        'form'       : 'gtt',
        'unit'       : 'ml',
        'quantity'   : 100,
        'total_price': 194.0,
        },
    {
        'name'       : 'Bromhexin',
        'form'       : 'tbl',
        'unit'       : 'ml',
        'quantity'   : 100,
        'total_price': 194.0,
        },
    {...},
    {...},
    ...,
    ]
```

### možnosti výstupu

- Pillow
- docx writer
- xls writer
- html/css
- latex/postscripts
