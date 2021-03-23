# String / Zeichenketten

Zeichenketten sind Folgen von Zeichen aus einem Alphabet (Zeichenketten Literale).



```py
# kurze Zeichenkette
"Text"
'Text'

# lange Zeichenkette
"""
langes
Text ...
"""

```

## Escape

```py
# \\ - Backslash in einem String
"Backslash\\"    # Backslash\

# \' - Hochkomma in einem String
"\'Hochkomma\'"  # 'Hochkomma'

# \" - Anführungszeichen in einem String
"\"Zitat\""      # "Zitat"

# \n - Zielenumbruch (line feed)
"eins\nzwei"    # eins
                # zwei

# \N{Name} - Zeichen mit einem Namen aus der Unicode-Datenbank
"\N{CYRILLIC CAPITAL LETTER ZHE}"
print("\N{CYRILLIC CAPITAL LETTER ZHE}") # ж

# \t - Horizontaler Tabulator
"eins \t zwei"    # eins    zwei

# \uxxxx - Zeichen, dessen 16-Bit-Unicode-Nummer durch eine vierstellige Hexadezimalzahl xxxx angegeben wird
"\u0416"

```
