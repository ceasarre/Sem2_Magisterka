import socket
import sys
from time import monotonic, time, sleep

# tworzymy gniazdo (adresacja IPv4, przeysłanie danych - strumieniowo)
try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Błąd przy tworzeniu gniazda")
    sys.exit()
print("Utworzono socket poprawnie!")

#definicja adresu oraz portu hosta
host_name = "localhost"
port = 2500

# próba utworzenia połączenia
try:
    soc.connect((host_name, port))
    print("Nawiązano połączenie z %s na porcie %s" %(host_name, port))
except socket.gaierror:
    print("Błąd związany z adresem podczas łączenia z serwerem")
    sys.exit()
except socket.error:
    print("Błąd podczas nawiązywania połączenia")
    sys.exit()

# próba odebrania i przesyłania danych
try:
    data = soc.recv(4096)
    print("Otrzymano od serwera: %s" %(str(data.decode('utf-8'))))

    message_to_server = input("Prześlij komunikat do serwera..")

    while True:

        # Aktualny czas
        
        print("Przesyłam do serwera dane: " + message_to_server)
       
        start = monotonic()
        print(start)
        soc.send(message_to_server.encode('utf-8'))
        
        sleep(1)
        data = soc.recv(4096)

        stop = monotonic()
        print(stop)
        delta = stop - start
        print("Otrzymano od serwera dane: " + data.decode() + " \n Czas otrzymania odpowiedzi: {} ".format(delta))

        message_to_server = input("Wpisz kolejną wiadomość do serwera. Jeśli chcesz zakończyć komunikację wpisz: 'koniec'")
        if message_to_server.lower() == 'koniec':
            break
    
    
    soc.send(message_to_server.encode())
    print("Przesłano do serwera: %s" %(message_to_server))

    response = soc.recv(4096)
    if response:
        print("Otrzymano od serwera: %s" % (str(response.decode('utf-8'))))
except socket.error:
    print("Błąd podczas komunikacji z serwerem")
    sys.exit()

# zakończenie połączenia
print("Zakończono połączenie")
soc.close()