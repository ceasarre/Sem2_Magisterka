import socket
import sys
import datetime

# tworzymy gniazdo i otwieramy port 1234, do którego gniazdo zostaje podpięte
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))
    # serwer nasłuchuje danych, które będą na port 1234 docierać (1 równoczesne połączenie do obsłużenia)
    server_socket.listen(1)
except:
    print("Nie udało się otworzyć gniazda..")
    sys.exit()

while True:
    print("Serwer oczekuje na połączenie..")
    try:
        client_socket, address = server_socket.accept()

        print("Nawiązano połącznie z klientem: %s" %(str(address)))

        # przesłanie wiadomości do klienta

        # Pobranie aktualnego czasu:
        hours = "Aktualna data i czas : {}".format(datetime.datetime.now())

        client_socket.send(bytes(hours, 'utf-8'))
        

        client_socket.close()
        print("Zakończono połączenie z klientem.")
    except:
        print("Zerwano połączenie z klientem..")


server_socket.close()