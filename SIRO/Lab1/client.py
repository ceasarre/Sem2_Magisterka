import socket
import sys
import os

DIR_NAME = '.'
FILE_NAME = 'res.txt'

# tworzymy gniazdo (adresacja IPv4, przeysłanie danych - strumieniowo)
try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Błąd przy tworzeniu gniazda")
    sys.exit()
print("Utworzono socket poprawnie!")

#definicja adresu oraz portu hosta
host_name = "localhost"
port = 1234

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

# próba przesłania danych do serwera
try:
    text_to_send = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host_name
    soc.send(text_to_send.encode())
    print("Przesłano do serwera: %s" %(text_to_send))
except socket.error:
    print("Błąd podczas przesyłania danych")
    sys.exit()

# próba odebrania danych przychodzących
try:
    data = soc.recv(4096)
    print("Otrzymano od serwera: %s" %(data.decode('utf-8')))

    # Zapis do pliku
    with open(os.path.join(DIR_NAME, FILE_NAME), 'w', encoding='utf-8') as f:
        f.write(data.decode('utf-8'))


except socket.error:
    print("Błąd podczas odbierania danych")
    sys.exit()

# zakończenie połączenia
print("Zakończono połączenie")
soc.close()
