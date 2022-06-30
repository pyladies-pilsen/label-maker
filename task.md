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

Tato možnost bude v praxi nejspíše těžko použitelná. Málo kdy bude potřeba vytvořit jen jednu cedulku.  
Bylo by to také zbytečné plýtvání papírem, jelikož aplikace generuje celé A4.

```commandline
python label_maker.py --nazev Bromhexin --jednotka ml --mnozstvi 100 --cena 194
```

### Omezení vstupu jednotlivých polí

Pole by měly umožňovat validaci vstupu.  
Uživatel bude upozorněn na špatně zadanou hodnotu.

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

- soubor s cedulkami připravený pro tisk  
  formát `docx` pro maximální kompatibilitu a snadné úpravy před tiskem
- seznam vygenerovaných cedulek  
  jednoduchý `txt` soubor pro kontrolu a případnou inventuru
- csv soubor který je možnost programem znovu načíst  
  umožní snadné úpravy a zrychlí zadávání druhé a každé další várky cedulek

---

## Technické informace:

### tvar dat za vstupem

Vstupní metody vrací výstup ve tvaru list slovníků.  
Umožní to tak kompatibilitu jednotlivých vstupu s dalším zpracováním.  
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