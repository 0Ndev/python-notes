## Liste

In einer Liste sind **mehrere Objekte (meistens von gleichen Typ) zusammengefasst**.

Liste kann Objekte völlig unterschiedlicher Typen und Variablen enthalten (genau wie Tupel).

Typisches Merkmal einer Liste ist, dass sie sich ständig ändert.


### Alltags Liste

- Bestellerliste des Buchhandels
- Hörercharts
- Abonnentenliste

<br>

```py
[1, 2, 3, 4, 5]

tageszeiten = ["Morgen", "Mittag", "Abend"]

# unterschiedliche Typen
liste = ["Text", 2, (1, 2)]

# multilisten struktur
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l[0] # [1, 2, 3]

s = [1, 2, 3]
s.append(4)  # [1, 2, 3, 4]

# von hinten zählen
s[-1]  # 4 letzte Element 
s[-2]  # 3 vorletzte Element

# Länge
len(s)  # 4 

len("") # 0 (leere Sequenz)

len(123) # Error - Zahlen haben keine Länge

```

<br>

### Unterschied zwischen Tupeln und Listen

Listen kann man verändern, Tupeln aber nicht.

<br>

## Konkatenation

Sequenzen gleicher Datentyps können konkateniert werden (einandergehängt).

So ein String kann nicht an eine Liste angehängt werden.

:x: `["König", "Dame"] + "Bauer"`

:white_check_mark:  `["König", "Dame"] + ["Bauer"]`

<br>

## Vervielfältigung

Ausdrücke wie **`s * n`** und **`n * s`** liefern eine neu Sequenz des gleichen Typs wie **s**, die durch **n**-maliges Aneinaderhängen der Sequenz **s** gebildet wird.

### :pushpin: Merke:
- nur positive Ganzzahlen (int) verwenden 
- Sequenz kann beliebigen Typ haben

### Beispiel

```py
0 * 'Hi'  # ''

3 * 'Hoch ' # Hoch Hoch Hoch

('an', 'aus') * 2  # ('an', 'aus', 'an', 'aus')

3 * [1]  # [1, 1, 1]

```
