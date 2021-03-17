# Rekursion

Eine rekursive Funktion ist eine Funktion, die sich selbst aufruft.

Es ist eine andere Methode, eine Schleife zu verwenden und meistens wenn sich die Parameter bei jedem Aufruf ändern sollen.

Rekursion ermöglicht kurze und elegante Formulierung der Problemlösungen.


:memo: Eine rekursive Funktion muss eine **bedingte Anweisung** enthalten, die den **Abbruch der Rekursion** ermöglicht. Ansonsten kommt es zu eine Endlosrekursion.


## Problemlösung mit Rekursion

- falls das aktuelle Problem einen einfachen Fall darstellt, löse es direkt     
- ansonsten teile es in Teilprobleme auf und wende dieselbe Strategie auf sie an

## Arten

- **Endrekursion** ist die einfache Form der Rekursion und kann auch leicht mit einer while-Schleife implementiert werden

## Rekursion Beispiele

- unendlich große Personengruppen (Vorfahren)

    | "Meine Vorfahren sind meine Eltern und die Vorfahren meiner Eltern."

- Spiegelbild des Spiegelbildes (Endlosrekursion)

- Kaleido-Spirale (Größe, Winkel und Position des Kreises ändert sich jedes Mal wenn die Funktion sich selbst aufruft)

## Nachteile rekursiver Funktion

- benötigen viel Speicherplatz, um Zwischenzustände der rekursiven Funktionsaufrufe zu speichern

- arbeiten häufig ineffizient (lange Laufzeiten) d.h. überflüssigerweise wird dieselbe Rechnung mehrfach durchgeführt.

<br>


### :computer: Code Beispiele

```py
# einfache Form der Rekursion (Endrekursion)
def spirale(x):
    if x < 5:
        return             # Abbruch der Rekursion
    else:
        forward(x)
        right(90)
        spirale(0.9 * x)   # rekursiver Aufruf
        return


# rekursive Zahlenfunktionen
# Fakultät
def factorial(n):
    # Abbruchbedingung (ansonsten Endlosrekursion)
    # base case: 1! = 1
    if n == 1:
        return 1
    else:
        # rekursive Aufruf
        # recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

factorial(20)


# Fibonacci Zahlen
i = 0
def fibonacci(n):
    global i
    i += 1
    print("Aufruf Nr.: ", i, " fib(",n,")")
    # Abbruchbedingung
    if n in [1, 2]:
        return 1
    # Abbruch der Rekursion
    else:
        return fib(n-2) + fib(n - 1) # rekursive Aufruf

fib(5)

```

Die Anzahl der rekursiven Aufrufe bezeichnet man als **Rekursionstiefe**.

