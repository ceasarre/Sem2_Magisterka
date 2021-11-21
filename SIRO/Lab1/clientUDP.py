import socket
import sys

# tworzymy gniazdo (adresacja IPv4, przeysłanie danych - datagramy)
try:
    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print("Błąd przy tworzeniu gniazda")
    sys.exit()
print("Utworzono socket poprawnie!")

#definicja adresu oraz portu hosta
udp_server_host = 'localhost'
udp_server_port = 2000

# wiadomość do przesłania do serwera
message_to_server = "Witaj, tutaj klient!"

try:
    print("Przesyłam do serwera dane: " + message_to_server)
    udp_client_socket.sendto(message_to_server.encode('utf-8'), (udp_server_host, udp_server_port))

    data, address = udp_client_socket.recvfrom(16)
    print("Otrzymano od serwera dane: " + data.decode())

except socket.error:
    print("Komunikacja z serwerem się nie powiodła..")

udp_client_socket.close()