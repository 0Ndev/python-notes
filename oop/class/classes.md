# Klassen

Klasse ist ein **Bauplan für Objekte** und beschreiben der prinzipielle Aufbau und das Verhalten einer Menge von Objekten. 

In Klassen sind Attribute und Methoden definiert.

## Objekte

Objekt ist eine **Instanzen (Inkarnation) einer Klassen** (gehört immer zu einer bestimmten Klasse).

Objekte repräsentieren Dinge der realen Welt und haben gewisse gemeinsame Merkmale.

Ein Objekt befindet sich zu jedem Zeitpunkt seiner Existenz in einem bestimmten Zustand. Der Zustand ergibt sich aus den momentanen Werten der Attribute.

Es ist auch möglich **Objekte ohne Namen** zu generieren (**Anonyme Objekte**).


### Attribute

Attribute beschreiben die **Merkmale eines Objektes**. 

Ein Attribut besteht aus einem Attributname und einem Attributwert (ein Attribut ist mit einem Wert belegt). 

Alle Objekte einer Klasse besitzen die gleichen Attributname, aber möglicherweise unterschiedlichen Attributwert.

**Klassenattribute (Klassenvariablen)** sind Merkmale, die alle Objekte einer Klasse besitzen.  
Sie haben gleichen Wertbelegung für alle Instanzen einer Klasse.


### Methoden

Methoden sind keine selbständige Objekte, sondern integraler Bestandteil einer Klasse. 

Es gibt öffentliche und private Methoden.


### Initialisierungsmethode

In der Initialisierungsmethode werden Objektattribute mit einem Wert belegt.

`__init__()` wird aufgerufen wenn ein Objekt der Klasse instanziiert wird.


:memo: Note:        
Das Argument `self` soll bei jeder Methode enthalten sein. Es bezeichnet das konkrete Objekt (Instanz).

### Statische Methoden

Statische Methoden einer Klasse können aufgerufen werden, ohne vorher eine Instanz zu erzeigen.

Meistens werden sie verwendet, um eine **Sammlung thematisch zusammengehöriger Operationen** zu programmieren (**toolbox**).


## Sichtbarkeit (Zugriff auf Attribute)

Der Zugriff auf Klassen und Objektattribute kann eingeschränkt werden.

Es gibt zwei unterschiedliche Attributarten:

- öffentliche

- private 

Ein Objekt sollte so wenig wie möglich über seinen internen Aufbau verraten.


### Öffentliche Attribute

Auf Öffentliche Attribute kann man von außen zugreifen und somit das Geheimprinzip verletzen, daswegen werden sie eher vermieden.


### Private Attribute

Attribute von außen schützen:

- **stark private Attribute** (private)

    | von außen abgeschirmt     
    Zugriff nur möglich innerhalb der Klassedefinition 

- **schwach private Attribute** (protected)

    | von außen problemlos zugreifbar       
    
    werden nicht in den Namensraum durch `from ... import *` importiert und somit verringern das Risiko von Namenskollisionen

Bei privaten Attributen müssen zusätzliche getter- und setter-Methoden definiert werden.        
Dadurch ist Code besser und sicherer, aber länger. 

Es ist auch möglich während des Programmlaufs neue Attribute zu erzeugen (dynamische Erzeugung), aber dieses Feature ist eine potenzielle Fehlerquelle.


<br>

### :computer: Beispiele

```py
class A:
    def __init__(self):
        self.__protected = "voll privat"
        self._privat = "schwach privat"
        self.public = "öffentlich"

    # private methode
    def _machdies():
        pass
    
```
