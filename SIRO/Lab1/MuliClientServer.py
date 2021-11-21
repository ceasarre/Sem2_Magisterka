import socket
from _thread import *
import sys
import threading

# tworzymy gniazdo i otwieramy port 2500, do którego gniazdo zostaje podpięte
try:
    multiserver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    multiserver_socket.bind(('localhost', 2500))

    multiserver_socket.listen(5)
except:
    print("Nie udało się otworzyć gniazda..")
    sys.exit()

disconnect_msg = 'koniec'

def client_handler(conn, addr):
    msg = "Witaj %s na serwerze obsługującym wielu klientów!" %(str(addr))
    conn.send(msg.encode('utf-8'))
    while True:
        data = conn.recv(4096)
        data = data.decode('utf-8')

        if data:
            if data == disconnect_msg:
                break
            else:
                msg_to_send = "Echo: " + data
                conn.send(msg_to_send.encode('utf-8'))
    print("Zakończono połączenie z klientem %s" %(addr))
    conn.close()


while True:
    print("Serwer oczekuje na połączenie..")
    try:
        client_socket, address = multiserver_socket.accept()

        print("Nawiązano połącznie z klientem: %s" %(str(address)))

        thread = threading.Thread(target=client_handler, args=(client_socket, address))
        thread.start()
        print("Liczba watków: " + str(threading.active_count()-1))

    except:
        print("Zerwano połączenie z klientem..")

multiserver_socket.close()
