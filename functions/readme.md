## Funktionen

Eine Funktion ist ein **Codeblock**, um eine Reihe von Anweisungen zu gruppieren und mehr als einmal in einem Programm zu verwenden können. 

Funktion wird nur dann ausgeführt, wenn sie aufgerufen wird.

Man kann Daten, sogenannte **Parameter**, an eine Funktion übergeben und dadurch werden Daten zurückgeben. 

Damit eine Funktion einen Wert zurückgibt, verwende die **return-Anweisung**. 

Es gibt auch **Standartfunktionen**, sogenannte ***built-in-function*s**, die immer verfügbar sind und für häufig vorkommende Aufgaben verwendet werden.

Außerdem gibt es **Module**, die weitere ***spezielle Funktionen*** enthalten.

### Parameter

Eine einzelne Information, die an einer Funktion übergeben wird.

#### Voreingestellte Parameter

Das sind **optionale Argumente**, die bei einem Aufruf weggelassen werden können.

Bei der Definition der Funktion werden optionale Argumente mit bestimmte **Default-Werte** voreingestellt und verwendet wenn beim Aufruf der Funktion das betreffende Argument fehlt.


### Rückgabe

Daten, die von der Funktion zurück an den Code übergeben werden.

---

### Funktionaufrufe

- **call by value**
```
- es wird eine Kopie übergeben, 
  diese kann in der aufgerufenen Funktion geändert werden.
- Originalobjekt bleibt unverändert
```

- **call by reference**
```
- Zeiger/Referenz auf ein Objekt
- es wird ein Zeiger auf die Daten übergeben  
- Der Zeiger (Pointer) ist nicht Konstant und kann verändert werden.      
- Originalobjekt wird verändert
```

- **call by object**
```
- je nach Datentyp kann ein Objekt von einer Funktion verändert werden oder nicht     
- (veränderbare Objekte wie z.B. Listen und unveränderbare z.B. Zahlen)
```

---

[Link zu Rekursion](recursion/recursion.md)

