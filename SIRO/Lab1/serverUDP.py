import socket
import sys

# tworzymy gniazdo i otwieramy port 2000, do którego gniazdo zostaje podpięte
try:
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server_socket.bind(('localhost', 2000))

except:
    print("Nie udało się otworzyć gniazda..")
    sys.exit()


while True:
    print("Serwer oczekuje na połączenie..")

    try:
        data, address = udp_server_socket.recvfrom(4096)
        print("Otrzymano od kiletna dane: ")
        print(str(data.decode()))

        message_to_send = "Witam, tutaj serwer!"
        print("Wysyłam do klietna następujące dane: " + message_to_send)

        udp_server_socket.sendto(message_to_send.encode('utf-8'), address)
    except socket.error:
        print("Komunikacja z klientem się nie powiodła..")


udp_server_socket.close()