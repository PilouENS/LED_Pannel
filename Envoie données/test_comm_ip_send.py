import socket

# Adresse IP de la STM32
IP_STM32 = "192.168.1.113"  # ou celle que tu as configurée
PORT = 12345               # même port que dans udp_bind()

message = "Image1 RGB R B"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(message.encode(), (IP_STM32, PORT))
print(f"Message envoyé à {IP_STM32}:{PORT}")
