```

█▀▀█ █░░█ █▀█ █▀▀▄ ▄▀▀▄ ░█▀█░ 　 ▒█▀▀▀█ ▒█░▒█ ▒█▀▀▀ ▒█░░░ ▒█░░░ 
█░░█ █▄▄█ ░▄▀ █▀▀▄ █▄▄░ █▄▄█▄ 　 ░▀▀▀▄▄ ▒█▀▀█ ▒█▀▀▀ ▒█░░░ ▒█░░░ 
█▀▀▀ ▄▄▄█ █▄▄ ▀▀▀░ ▀▄▄▀ ░░░█░ 　 ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄█    v.0.2
```

Python Shell w/ B64 Encoding (Custom) - Bind Shell PoC

An interpreter needs both the 1. server.py, and 2. client.py to be able to permit a more realistic test. 

Use a portable python interpreter like https://github.com/EdwardLab/binpython/releases/tag/0.46 to get the best results.

Run on the target host:

Note: The hardcoded IPs are in client.py

```
Uage: pyton3 server.py
Uage: python3 client.py
```

The HOST and PORT are hardcoded and need to be changed.

Hardcoded variables to change:

```
HOST = '192.168.1.67'  # The IP of the listener.
PORT = 446              # The same port as listener.
```

---

Updates (4/15/25)
The client has been updated to change the IP and PORT. Also a compiled exe version has been included.

The server source hasnt been changed but an exe version that listens on port 446 has been added.

---

Features: Custom encode commands before they are sent to the server.

By LiquidSky @ S3 (c) 2025

This is for educational purposes and legitimate testing.
