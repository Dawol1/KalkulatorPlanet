# Kalkulator odległości planet od słońca
## Prosty kalkulator do obliczania odległości planet od Słońca na podstawie trzeciej zasadzie dynamiki Newtona i prawa Keplera o ruchu planet.
Aby uruchomić program, który będzie realizował obliczanie odległości planet od Słońca należy otworzyć folder z kodem w wybranym środowisku programistycznym, np. PyCharm.

Upewnij się, że masz zainstalowaną bibliotekę flask.

Jeśli nie zainstaluj ją w następujący sposób:

1. Otwórz terminal lub wiersz polecenia.
2. Wpisz poniższą komendę i naciśnij Enter, aby zainstalować Flask:

```bash
pip install Flask
```

Następnie otwórz plik main.py oraz uruchom funkcję main.

Program zostanie uruchomiony i będzie dostępny pod adresem
```bash
http://127.0.0.1:5000
```

Aby sprawdzić odległość dla danej planety należy wejść pod adres:
```bash
http://127.0.0.1:5000/distance/{Nazwa_Planety}
```

Przykład użycia programu dla Marsa:
```bash
http://127.0.0.1:5000/distance/Mars
```

Wynik działania programu:
```plaintext
{"distance_au":1.52,"distance_km":227961594.34,"planet":"Mars"}
```