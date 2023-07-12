import socket
import sys

# Adres i port serwera
SERVER_ADDRESS = "localhost"
SERVER_PORT = 1234

# Inicjalizacja gniazda serwera
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
server_socket.listen(2)

# Inicjalizacja graczy
players = []

# Oczekiwanie na połączenie dwóch graczy
def wait_for_players():
    while len(players) < 2:
        print("Oczekiwanie na połączenie gracza...")
        client_socket, client_address = server_socket.accept()
        players.append(client_socket)
        print("Gracz połączony:", client_address)

# Obsługa komunikacji z klientami
def handle_communication():
    while True:
        for player_socket in players:
            try:
                message = player_socket.recv(1024).decode()
                print("Wiadomość od gracza:", message)
                # Tutaj można dodać odpowiednią logikę obsługi wiadomości
            except socket.error:
                print("Błąd podczas odbierania wiadomości")
                sys.exit()

# Główna pętla serwera
def server_loop():
    wait_for_players()
    handle_communication()

# Uruchomienie serwera
if __name__ == "__main__":
    server_loop()
