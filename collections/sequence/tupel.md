## Tupel

In einem Tuple werden **mehrere Objekte** eventuell **unterschiedlicher Typen zu einem komplexen Objekt zusammengefasst**.

### Alltags Tupel

- Name und Geburtsdatum einer Person
- dreidimensionales Koordinatensystem (Tripel aus x-, y- und z-Komponenten)
- Adresse (Name, Straße, Hausnummer, Postlerzahl, Stadt)
- Beschreibung einer Farbe durch Angabe von Rot-, Grün- und Blau-Komponente

### Beispiel

```py
("Ampel", 3 ('rot', 'gelb', 'grün'))

t = 1, 2, 3
print(t)    # (1, 2, 3)

name = "Jo"
greeting = "Hello"
greet = name, greeting
print(greet[0])  # Jo

```

