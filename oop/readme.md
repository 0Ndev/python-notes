# Objektorientierte Programmieren

Ein objektorientiertes Programm ist ein System von Objekten, die untereinander Botschaften austauschen.



Zur visuellen Beschreibung von objektorientierten Programmen werden häufig die grafischen Symbole von **UML** (Unified Modeling Language) verwendet.


## Abstraktion

Die wesentliche Aspekte einer Sache ermitteln und das Unwichtige (unwesentliche Daten) weglassen.

## Verkapselung (encapsulation)

Operationen und logisch zusammengehörige Daten (Attribute) werden zu einer Einheit (einer Klasse) verschmolzen.

## Geheimprinzip (information hiding)

Der Zustand eines Objektes (Werte der Attribute) und die Implementierung der Methoden sind nach außen nicht sichtbar.   
Alle Attribute sind streng privat.

Änderungen des Zustandes eines Objektes können von außen nur über Methodenaufrufe (Botschaften) ermöglicht werden. 

## Vererbung

Vererbung beschreibt die **Beziehung zwischen einer allgemeinen Klasse** (Basisklasse, Oberklasse) **und einer spezialisierten Klasse** (Subklasse, Unterklasse). 

Die Subklasse besitzt sämtliche Attribute und Methoden der Basisklasse und können zusätzliche Attribute und Methoden haben. Die Methoden können durch Überschreiben(overriding) neu definiert werden.

## Spezialisierungen

Von einer Basisklasse können spezielle Subklassen gebildet werden.

---

## Polymorphismus

Polymorphismus ermöglicht den **gleichen Namen** für (mehr oder weniger) gleichartige Operationen zu verwenden, um dann es **auf Objekte unterschiedlicher Klassen anzuwenden**.        
Man spricht von einer **Überladung** (**overloading**) einer Operation.

Ein Beispiel dafür ist der **Plusoperator**, der durch die Methode `__add__()` repräsentiert wird und auf Zahlen oder Strings angewendet werden kann. Je nach Datentyp wirkt `+ ` als Addition oder Konkatenation.

Ein weiteres Beisiel ist die `__init__()` Methode, die eine Überladung der Zuweisungsoperators `= `verwendet wird, um eine Instanz einer Klasse zu bilden.

---
<br>

### :computer: Beispiel

```py


```


```py

```


