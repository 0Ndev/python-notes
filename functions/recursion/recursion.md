# Rekursion

Eine rekursive Funktion ist eine **Funktion, die sich selbst aufruft**.

Es ist eine andere Methode, eine Schleife zu verwenden und meistens wenn sich die Parameter bei jedem Aufruf ändern sollen.

Mithilfe von Rekursion hat man früher Schleifen geschrieben, also Rekursion ist eine Urschleife.

Rekursion ermöglicht kurze und elegante Formulierung der Problemlösungen.


:memo: Eine rekursive Funktion muss eine **bedingte Anweisung** enthalten, die den **Abbruch der Rekursion** ermöglicht. Ansonsten kommt es zu eine Endlosrekursion.


## Problemlösung mit Rekursion

- falls das aktuelle Problem einen einfachen Fall darstellt, löse es direkt     
- ansonsten teile es in Teilprobleme auf und wende dieselbe Strategie auf sie an

## Arten

- **Endrekursion** ist die einfache Form der Rekursion und kann auch leicht mit einer while-Schleife implementiert werden

## Rekursion Beispiele

- unendlich große Personengruppen (*Vorfahren*)

    | "Meine Vorfahren sind meine Eltern und die Vorfahren meiner Eltern."

- *Spiegelbild des Spiegelbildes* (Endlosrekursion)

- *Kaleido-Spirale* (Größe, Winkel und Position des Kreises ändert sich jedes Mal wenn die Funktion sich selbst aufruft)

- Manche *Sortieralgorithmen* sind rekursive (Turm von Hanoi, Quick Sort, alle fraktalen Strukturen).

## Nachteile rekursiver Funktion

- benötigen viel Speicherplatz, um Zwischenzustände der rekursiven Funktionsaufrufe zu speichern

- arbeiten häufig ineffizient (lange Laufzeiten) d.h. überflüssigerweise wird dieselbe Rechnung mehrfach durchgeführt.

<br>


### :computer: Code Beispiele

```py
# rekursive Zahlenfunktionen

# Fakultät (factorial)
def fact(n):
    # base case: !0 = 1
    if n == 0:
        return 1
    # recursive case: n! = n * (n-1)!
    return n * fact(n -1)

result = fact(5)
print(result) # 120

# Erläuterung (explanation)
fact(5) ->  5 * 4!  ->  5 * 24 = 120
fact(4) ->  4 * 3!  ->  4 * 6 = 24
fact(3) ->  3 * 2!  ->  3 * 2 = 6
fact(2) ->  2 * 1!  ->  2 * 1 = 3
fact(1) ->  1 * 0!  ->  1 * 1 = 1
fact(0) ->  !0 = 1


# Fakultät andere Bsp.
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


# einfache Form der Rekursion (Endrekursion)
def spirale(x):
    if x < 5:
        return             # Abbruch der Rekursion
    else:
        forward(x)
        right(90)
        spirale(0.9 * x)   # rekursiver Aufruf
        return


# Rekursion geht vor und dann wieder zurück
def rek(x):
    if x < 10:
        print("1) x = ", x)
        x=x+1
        rek(x)
        print("2) x = ", x)

def main():
    x=0
    rek(x)

main()

# ausgabe:
1) x = 0    # das ist der Punkt wo sich der Stack aufbaut
1) x = 1
...
1) x = 9    
2) x = 10   # ruft es sich auf, kommt aber nicht ins if rein
2) x = 9    # Stack baut sich wieder ab 
... 
2) x = 1

```

Die Anzahl der rekursiven Aufrufe bezeichnet man als **Rekursionstiefe**.

