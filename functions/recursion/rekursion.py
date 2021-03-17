"""
Rekursion

Mithilfe von Rekursion hat man früher Schleifen geschrieben, also Rekursion ist eine Urschleife.

Stack (Stapelspeicher oder Kellerspeicher) baut sich auf und dann wieder ab.
In Stack wird eine neue Variable platziert , d.h. Kopie wird über Kopie aufeinander aufgesetzt (Aufruf).

Stack (Stapelspeicher oder Kellerspeicher) wird häufig eingesetzte dynamische Datenstruktur.

Manche Sortieralgorithmen sind rekursive. 
"""

# Vorteil dieser Schleife ist das sie vorwärts und dann wieder zurück geht.
def rek(x):
    if(x < 10):
        print("1) x =", x)
        x=x+1
        rek(x)
        print("2) x =", x)

def main():
    x=0
    rek(x)

main()


"""
Ausgabe:
1) x = 0    # das ist der Punkt wo sich der Stack aufbaut
1) x = 1
1) x = 2
1) x = 3
1) x = 4
1) x = 5
1) x = 6
1) x = 7
1) x = 8
1) x = 9    # ruft es sich auf, kommt aber nicht ins if rein
2) x = 10   # Stack baut sich wieder ab 
2) x = 9    
2) x = 8
2) x = 7
2) x = 6
2) x = 5
2) x = 4
2) x = 3
2) x = 2
2) x = 1
"""
