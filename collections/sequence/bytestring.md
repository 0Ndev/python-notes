# Bytestrings

Bytestrings sind **Folgen von Zahlen zwischen 0 und 255**.

Diese Zahlen werden im Bytestring-Literal und möglich auch als ASCII-Zeichen dargestellt.

Bytestrings sind genau so wie Strings **unveränderbar**.

---

### ASCII (American Standart Code for Inforamtion Interchange) 

**ASCII** codiert Buchstaben, Ziffern und Satzzeichen (insgesamt 95 druckbare zeichen) durch **Nummern zwischen 0 und 127**.

---

Wenn für eine Zahl kein ASCII-Zeichen existiert (z.B. 128, 129), erscheint an dieser Stelle im Bytestring eine Escape-Sequenz, die die Zahl als Hexadezimalzahl wiedergibt.


```py
b = bytes([100, 101, 128, 129]) # b'de\x80\x81

b = b'abc
b[0] # 97 (erstes item ist a)
```

