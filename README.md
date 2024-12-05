# Ping-Pong Python Application

## Projektbeschreibung

Dieses Projekt implementiert einen einfachen Ping-Pong-Service mit Python. Der Ping-Dienst sendet eine Zahl `n`, und der Pong-Dienst antwortet mit `n + 1`. Ausserdem gibt es die Möglichkeit `proxy.py` als "middleman" einzusetzen. Dieser empfänsgt die Zahl von `ping.py` und sendet diese ohne zu Verändern an `pong.py`, das gleiche umgekehrt.

## Voraussetzungen

- Python 3.7 oder neuer
- Socket-Kommunikation aktiviert

## Installation

1. Klone das Repository:
   ```bash
   git clone https://github.com/FaKiieZ/ping-pong.git
   cd ping-pong
   ```

## Ausführen
**Achtung**: In Debian ist "python" mit "python3" zu ersetzen!
### Standard Ping-Pong
1. Wechsle in das Verzeichnis `src` mit dem Befehl `cd src`.
2. Führe den Befehl `python pong.py` aus.
3. Führe in einem neuen Terminal den Befel `python ping.py` aus.
4. Port vom pong-server angeben.

### Ping-Pong mit Proxy
1. Wechsle in das Verzeichnis `src` mit dem Befehl `cd src`.
2. Führe den Befehl `python pong.py` aus.
3. Führe in einem neuen Terminal den Befel `python proxy.py` aus.
4. Führe in einem neuen Terminal den Befel `python ping.py` aus.



## Laufendes Programm beenden
Um den Server, Proxy oder auch Client (ping.py) zu beenden, kann ctrl+c gedrückt werden.
