# Label maker - tvorba cenovek

> Tento projek je součástí navazujícího kurzu [pyladies Plzeň](https://pyladies.cz/plzen/).
> Možnosti vstupu, výstupu a chování aplikace je popsáno v [zadání](task.md).

## Popis projektu

Program, který usnadňuje práci při tvorbě cenovek v lékárně.

Uživatel zadá potřebné hodnoty, výsupem je pak tisknutelný soubor připravený k rozstříhání.

Script při každém běhu exportuje data do csv soboru, který je možné zpětně načíst.  
Generuje se také txt soubor s názvy cedulek pro kontrolu.

![ilustracni_foto_cedulky](_resources/vyplnena.jpg)

---

## Instalace

Momentálně je aplikace ve formě spustitelného python scriptu. Je tak potřeba mýt nainstalovaný python ve verzi 3.6 a
větší.  
Pro instalaci je také doporučeno použít virtuální prostředí, například vestavěné `venv`.

Instalaci pythonu ověříme v příkazové řádce pomocí příkzu: `where.exe python`.

Poté v příkazové řádce instalujeme pomocí následujících příkazů:

```commandline
git clone https://github.com/pyladies-pilsen/label-maker
cd label-maker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Spuštění

> Poznámka: spouštíme vždy s aktivovaným virtuálním prostředím

### Příklad použití argumentů

#### Bez argumentu:

``` commandline
python label_maker.py
```

Pokud script spustíme bez argumentu, objeví se výzva k zadávání dat pro cedulky ručně.  
Použije se tamplate `templates/labels_template.docx`.  
Výstupní soubor bude ve složce `output`.

#### Vstup z předpřipraveného souboru

```commandline
python label_maker.py --from-file
```

Při použtí flagu `--from-file` script automaticky načte data ze souboru `input/input_data.csv`.  
Použije se tamplate `templates/labels_template.docx`.  
Výstupní soubor bude ve složce `output`.

Je možno zvolit jiný soubor pomocí příkazu:

```commandline
python label_maker.py --from-file --input-file input/moje_data.csv
```

#### Změna templatu

```commandline
python label_maker.py --template-file templates/jiny_template.docx
```

#### Výstup do konzole

```commandline
python label_maker.py --to-console
```

Objeví se výzva k zadávání dat pro cedulky ručně.
Výstup bude formátovaný text do konzole.  
Použitelné pro kontorlu.

#### Možnosti txt výstupu

K vygenerovanému txt souboru s názvy cedulek je možné přidat číslování a zaškrtávací políčka.

```commandline
python label_maker.py --txt-with-numbers  
python label_maker.py --txt-with-checkbox
```

Je možná i kombinace obojího.

```commandline
python label_maker.py --txt-with-numbers --txt-with-checkbox
```

```text
Seznam cedulek - celkem 10
--------------------------------------------------------------------------------
Bepanthen Seneiderm crm 50 g
  1. - Bepanthen Seneiderm crm 50 g
[ ] - Bepanthen Seneiderm crm 50 g
[ ] -   1. - Bepanthen Seneiderm crm 50 g
```

### Kombinace argumentu

Argumenty je možno libovolně kombinovat.  
Např.:

- `python label_maker.py --from-file --to-console`
- `python label_maker.py --from-file --input-file input/moje_data.csv`
- `python label_maker.py --from-file --txt-with-numbers --txt-with-checkbox`



