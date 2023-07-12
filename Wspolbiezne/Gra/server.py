# # # import socket
# # # import pickle
# # # import random
# # #
# # # # Inicjalizacja socketu serwera
# # # HOST = 'localhost'
# # # PORT = 12345
# # # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # # server_socket.bind((HOST, PORT))
# # # server_socket.listen(2)
# # #
# # # # Klasa GameServer
# # # class GameServer:
# # #     def __init__(self):
# # #         self.connections = []
# # #         self.players = []
# # #         self.board = [[None for _ in range(6)] for _ in range(6)]
# # #         self.turn = None
# # #
# # #     def accept_connections(self):
# # #         for _ in range(2):
# # #             conn, addr = server_socket.accept()
# # #             self.connections.append(conn)
# # #             print(f"Połączono z {addr}")
# # #             player_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# # #             self.players.append(player_color)
# # #             conn.send(pickle.dumps(player_color))
# # #
# # #     def send_message(self, conn, message):
# # #         conn.send(pickle.dumps(message))
# # #
# # #     def receive_message(self, conn):
# # #         data = conn.recv(4096)
# # #         if not data:
# # #             return None
# # #         return pickle.loads(data)
# # #
# # #     def update_board(self, row, col, player_index):
# # #         self.board[row][col] = self.players[player_index]
# # #
# # # def check_winner(self):
# # #     # Sprawdzenie wygranej w poziomie
# # #     for row in range(6):
# # #         consecutive = 0
# # #         last_color = None
# # #         for col in range(6):
# # #             if self.board[row][col] is not None:
# # #                 if last_color is None or self.board[row][col] == last_color:
# # #                     consecutive += 1
# # #                     last_color = self.board[row][col]
# # #                 else:
# # #                     consecutive = 1
# # #                     last_color = self.board[row][col]
# # #             else:
# # #                 consecutive = 0
# # #                 last_color = None
# # #             if consecutive == 6:
# # #                 return True
# # #
# # #     # Sprawdzenie wygranej w pionie
# # #     for col in range(6):
# # #         consecutive = 0
# # #         last_color = None
# # #         for row in range(6):
# # #             if self.board[row][col] is not None:
# # #                 if last_color is None or self.board[row][col] == last_color:
# # #                     consecutive += 1
# # #                     last_color = self.board[row][col]
# # #                 else:
# # #                     consecutive = 1
# # #                     last_color = self.board[row][col]
# # #             else:
# # #                 consecutive = 0
# # #                 last_color = None
# # #             if consecutive == 6:
# # #                 return True
# # #
# # #     # Sprawdzenie wygranej na ukos (lewa-gora do prawa-dol)
# # #     for i in range(3):
# # #         for j in range(3):
# # #             consecutive = 0
# # #             last_color = None
# # #             for k in range(6):
# # #                 row = i + k
# # #                 col = j + k
# # #                 if self.board[row][col] is not None:
# # #                     if last_color is None or self.board[row][col] == last_color:
# # #                         consecutive += 1
# # #                         last_color = self.board[row][col]
# # #                     else:
# # #                         consecutive = 1
# # #                         last_color = self.board[row][col]
# # #                 else:
# # #                     consecutive = 0
# # #                     last_color = None
# # #                 if consecutive == 6:
# # #                     return True
# # #
# # #     # Sprawdzenie wygranej na ukos (lewa-dol do prawa-gora)
# # #     for i in range(3):
# # #         for j in range(3, 6):
# # #             consecutive = 0
# # #             last_color = None
# # #             for k in range(6):
# # #                 row = i + k
# # #                 col = j - k
# # #                 if self.board[row][col] is not None:
# # #                     if last_color is None or self.board[row][col] == last_color:
# # #                         consecutive += 1
# # #                         last_color = self.board[row][col]
# # #                     else:
# # #                         consecutive = 1
# # #                         last_color = self.board[row][col]
# # #                 else:
# # #                     consecutive = 0
# # #                     last_color = None
# # #                 if consecutive == 6:
# # #                     return True
# # #
# # #     return False
# # #
# # #     def run(self):
# # #         self.accept_connections()
# # #         current_player = 0
# # #
# # #         while True:
# # #             for conn in self.connections:
# # #                 self.send_message(conn, self.turn)
# # #
# # #             move = self.receive_message(self.connections[current_player])
# # #             row, col = move
# # #             self.update_board(row, col, current_player)
# # #
# # #             for conn in self.connections:
# # #                 self.send_message(conn, self.board)
# # #
# # #             if self.check_winner():
# # #                 print("Wygrał gracz", current_player + 1)
# # #                 for conn in self.connections:
# # #                     conn.close()
# # #                 break
# # #
# # #             current_player = (current_player + 1) % 2
# # #             self.turn = not self.turn
# # #
# # #
# # # # Uruchomienie serwera
# # # if __name__ == '__main__':
# # #     game_server = GameServer()
# # #     game_server.run()
# #
# #
# # # import socket
# # # import pickle
# # # import random
# # #
# # # # Inicjalizacja socketu serwera
# # # import numpy as np
# # #
# # # HOST = 'localhost'
# # # PORT = 12345
# # # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # # server_socket.bind((HOST, PORT))
# # # server_socket.listen(2)
# # #
# # #
# # # # Klasa GameServer
# # # class GameServer:
# # #     def __init__(self):
# # #         self.connections = []
# # #         self.players = []
# # #         self.board = np.zeros((6, 6), dtype=object)
# # #         self.turn = False
# # #
# # #     def accept_connections(self):
# # #         for _ in range(2):
# # #             conn, addr = server_socket.accept()
# # #             self.connections.append(conn)
# # #             print(f"Połączono z {addr}")
# # #             player_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# # #             self.players.append(player_color)
# # #             conn.send(pickle.dumps(player_color))
# # #
# # #     def send_message(self, conn, message):
# # #         conn.send(pickle.dumps(message))
# # #
# # #     def receive_message(self, conn):
# # #         data = conn.recv(4096)
# # #         if not data:
# # #             return None
# # #         return pickle.loads(data)
# # #
# # #     def update_board(self, row, col, player_index):
# # #         self.board[row][col] = self.players[player_index]
# # #
# # #     def check_winner(self):
# # #         # Sprawdzenie wygranej w poziomie
# # #         for row in range(6):
# # #             consecutive = 0
# # #             last_color = None
# # #             for col in range(6):
# # #                 if self.board[row][col] is not None:
# # #                     if last_color is None or self.board[row][col] == last_color:
# # #                         consecutive += 1
# # #                         last_color = self.board[row][col]
# # #                     else:
# # #                         consecutive = 1
# # #                         last_color = self.board[row][col]
# # #                 else:
# # #                     consecutive = 0
# # #                     last_color = None
# # #                 if consecutive == 6:
# # #                     return True
# # #
# # #         # Sprawdzenie wygranej w pionie
# # #         for col in range(6):
# # #             consecutive = 0
# # #             last_color = None
# # #             for row in range(6):
# # #                 if self.board[row][col] is not None:
# # #                     if last_color is None or self.board[row][col] == last_color:
# # #                         consecutive += 1
# # #                         last_color = self.board[row][col]
# # #                     else:
# # #                         consecutive = 1
# # #                         last_color = self.board[row][col]
# # #                 else:
# # #                     consecutive = 0
# # #                     last_color = None
# # #                 if consecutive == 6:
# # #                     return True
# # #
# # #         # Sprawdzenie wygranej na ukos (lewa-gora do prawa-dol)
# # #         for i in range(3):
# # #             for j in range(3):
# # #                 consecutive = 0
# # #                 last_color = None
# # #                 for k in range(6):
# # #                     row = i + k
# # #                     col = j + k
# # #                     if self.board[row][col] is not None:
# # #                         if last_color is None or self.board[row][col] == last_color:
# # #                             consecutive += 1
# # #                             last_color = self.board[row][col]
# # #                         else:
# # #                             consecutive = 1
# # #                             last_color = self.board[row][col]
# # #                     else:
# # #                         consecutive = 0
# # #                         last_color = None
# # #                     if consecutive == 6:
# # #                         return True
# # #
# # #         # Sprawdzenie wygranej na ukos (lewa-dol do prawa-gora)
# # #         for i in range(3):
# # #             for j in range(3, 6):
# # #                 consecutive = 0
# # #                 last_color = None
# # #                 for k in range(6):
# # #                     row = i + k
# # #                     col = j - k
# # #                     if self.board[row][col] is not None:
# # #                         if last_color is None or self.board[row][col] == last_color:
# # #                             consecutive += 1
# # #                             last_color = self.board[row][col]
# # #                         else:
# # #                             consecutive = 1
# # #                             last_color = self.board[row][col]
# # #                     else:
# # #                         consecutive = 0
# # #                         last_color = None
# # #                     if consecutive == 6:
# # #                         return True
# # #
# # #         return False
# # #
# # #     def run(self):
# # #         self.accept_connections()
# # #         current_player = 0
# # #
# # #         while True:
# # #             for conn in self.connections:
# # #                 self.send_message(conn, self.turn)
# # #
# # #             move = self.receive_message(self.connections[current_player])
# # #             print("Received move from player", current_player + 1, ":", move)
# # #             row, col = move
# # #             self.update_board(row, col, current_player)
# # #
# # #             # if move is not None and len(move) == 2:
# # #             #     row, col = move
# # #             #     self.update_board(row, col, current_player)
# # #             # else:
# # #             #     print("Invalid move received from player", current_player + 1)
# # #             #     continue
# # #
# # #             for conn in self.connections:
# # #                 self.send_message(conn, self.board)
# # #
# # #             if self.check_winner():
# # #                 print("Wygrał gracz", current_player + 1)
# # #                 for conn in self.connections:
# # #                     conn.close()
# # #                 break
# # #
# # #             current_player = (current_player + 1) % 2
# # #             self.turn = not self.turn
# # #             print("Board:", self.board)
# # #
# # #
# # # # Uruchomienie serwera
# # # if __name__ == '__main__':
# # #     game_server = GameServer()
# # #     game_server.run()
# #
# #
# # import socket
# # import pickle
# # import random
# #
# # # Inicjalizacja socketu serwera
# # import numpy as np
# #
# # HOST = 'localhost'
# # PORT = 12345
# # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # server_socket.bind((HOST, PORT))
# # server_socket.listen(2)
# #
# #
# # # Klasa GameServer
# # class GameServer:
# #     def __init__(self):
# #         self.connections = []
# #         self.players = []
# #         self.board = np.zeros((6, 6), dtype=object)
# #         self.turn = False
# #
# #     def accept_connections(self):
# #         for _ in range(2):
# #             conn, addr = server_socket.accept()
# #             self.connections.append(conn)
# #             print(f"Połączono z {addr}")
# #             player_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# #             self.players.append(player_color)
# #             conn.send(pickle.dumps(player_color))
# #
# #     def send_message(self, conn, message):
# #         conn.send(pickle.dumps(message))
# #
# #     def receive_message(self, conn):
# #         data = conn.recv(4096)
# #         if not data:
# #             return None
# #         return pickle.loads(data)
# #
# #     def update_board(self, row, col, player_index):
# #         self.board[row][col] = self.players[player_index]
# #
# #     def check_winner(self):
# #         # Sprawdzenie wygranej w poziomie, pionie i na ukos
# #         for i in range(6):
# #             for j in range(6):
# #                 if self.board[i][j] is None:
# #                     continue
# #
# #                 # Sprawdzenie wygranej w poziomie
# #                 if j + 5 < 6 and all(self.board[i][j + k] == self.board[i][j] for k in range(6)):
# #                     return True
# #
# #                 # Sprawdzenie wygranej w pionie
# #                 if i + 5 < 6 and all(self.board[i + k][j] == self.board[i][j] for k in range(6)):
# #                     return True
# #
# #                 # Sprawdzenie wygranej na ukos (lewa-gora do prawa-dol)
# #                 if i + 5 < 6 and j + 5 < 6 and all(self.board[i + k][j + k] == self.board[i][j] for k in range(6)):
# #                     return True
# #
# #                 # Sprawdzenie wygranej na ukos (lewa-dol do prawa-gora)
# #                 if i - 5 >= -1 and j + 5 < 6 and all(self.board[i - k][j + k] == self.board[i][j] for k in range(6)):
# #                     return True
# #
# #         return False
# #
# #     def run(self):
# #         self.accept_connections()
# #         current_player = 0
# #
# #         while True:
# #             for conn in self.connections:
# #                 self.send_message(conn, self.turn)
# #
# #             move = self.receive_message(self.connections[current_player])
# #             print("Received move from player", current_player + 1, ":", move)
# #             if len(move) != 2:
# #                 print("Invalid move")
# #                 continue
# #
# #             row, col = move
# #             if self.board[row][col] is not None:
# #                 print("Invalid move")
# #                 continue
# #
# #             self.update_board(row, col, current_player)
# #
# #
# #             for conn in self.connections:
# #                 self.send_message(conn, self.board)
# #
# #             if self.check_winner():
# #                 print("Wygrał gracz", current_player + 1)
# #                 for conn in self.connections:
# #                     conn.close()
# #                 break
# #
# #             current_player = (current_player + 1) % 2
# #             self.turn = not self.turn
# #             print("Board:", self.board)
# #
# #
# # # Uruchomienie serwera
# # if __name__ == '__main__':
# #     game_server = GameServer()
# #     game_server.run()
#
#
# import socket
# import threading
# import pickle
#
# # Tworzenie serwera
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = ('localhost', 5555)
# server_socket.bind(server_address)
# server_socket.listen(2)
# print("Serwer nasłuchuje na porcie", server_address[1])
#
#
# class GameServer:
#     def __init__(self):
#         self.players = []
#         self.player_turn = 0
#         self.board = [[0 for _ in range(6)] for _ in range(6)]
#         self.game_over = False
#
#     def handle_client(self, player, player_number):
#         # Wysyłanie numeru przypisanego graczowi
#         player.send(pickle.dumps(player_number))
#
#         while True:
#             try:
#                 data = player.recv(4096)
#                 message = pickle.loads(data)
#
#                 # Aktualizacja planszy
#                 self.board[message['row']][message['column']] = message['player_number']
#
#                 # Sprawdzenie, czy któryś gracz wygrał
#                 win = False
#                 # Sprawdź wiersze
#                 for r in range(6):
#                     if all(self.board[r][c] == message['player_number'] for c in range(6)):
#                         win = True
#                         break
#                 # Sprawdź kolumny
#                 for c in range(6):
#                     if all(self.board[r][c] == message['player_number'] for r in range(6)):
#                         win = True
#                         break
#                 # Sprawdź przekątne
#                 if message['row'] == message['column'] and all(self.board[i][i] == message['player_number'] for i in range(6)):
#                     win = True
#                 if message['row'] + message['column'] == 5 and all(self.board[i][5 - i] == message['player_number'] for i in range(6)):
#                     win = True
#
#                 # Zmiana gracza, jeśli nie ma wygranej
#                 if not win:
#                     self.player_turn = (self.player_turn + 1) % 2
#
#                 # Sprawdzenie, czy plansza jest pełna
#                 if all(all(row) for row in self.board):
#                     self.game_over = True
#
#                 # Wysyłanie aktualizacji do obu graczy
#                 update = {'game_over': self.game_over, 'board': self.board, 'current_player': self.player_turn}
#                 player.send(pickle.dumps(update))
#                 self.players[self.player_turn].send(pickle.dumps(update))
#
#             except socket.error as e:
#                 print("Błąd podczas komunikacji z klientem:", e)
#                 break
#
#     def start_game(self):
#         while len(self.players) < 2:
#             player, address = server_socket.accept()
#             print("Nowe połączenie:", address)
#
#             self.players.append(player)
#             player_number = len(self.players)
#             print("Gracz", player_number, "dołączył do gry.")
#
#             if len(self.players) == 2:
#                 print("Gra rozpoczęta!")
#                 # Wysłanie informacji o stanie gry do obu graczy
#                 update = {'game_over': self.game_over, 'board': self.board, 'current_player': self.player_turn}
#                 self.players[0].send(pickle.dumps(update))
#                 self.players[1].send(pickle.dumps(update))
#
#                 # Uruchomienie wątku obsługującego pierwszego gracza
#                 thread_player1 = threading.Thread(target=self.handle_client, args=(self.players[0], 1))
#                 thread_player1.start()
#
#                 # Uruchomienie wątku obsługującego drugiego gracza
#                 thread_player2 = threading.Thread(target=self.handle_client, args=(self.players[1], 2))
#                 thread_player2.start()
#
#
# # Inicjalizacja serwera gry
# game_server = GameServer()
# game_server.start_game()
#

# import socket
# import pickle
#
# # Klasa GameServer
# class GameServer:
#     def __init__(self, server_address):
#         self.server_address = server_address
#         self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.client_connections = []
#         self.board = [[0 for _ in range(6)] for _ in range(6)]
#         self.current_player = 0
#         self.game_over = False
#
#     def start(self):
#         self.server_socket.bind(self.server_address)
#         self.server_socket.listen(2)
#
#         print("Oczekiwanie na połączenia graczy...")
#
#         while len(self.client_connections) < 2:
#             client_socket, client_address = self.server_socket.accept()
#             print("Połączono z", client_address)
#             self.client_connections.append(client_socket)
#
#         self.setup_game()
#
#     def send_message(self, client_socket, message):
#         client_socket.sendall(pickle.dumps(message))
#
#     def receive_message(self, client_socket):
#         data = client_socket.recv(1024)
#         return pickle.loads(data)
#
#     def setup_game(self):
#         for client_socket in self.client_connections:
#             self.send_message(client_socket, self.board)
#             self.send_message(client_socket, self.current_player)
#
#     def handle_move(self, client_socket):
#         move = self.receive_message(client_socket)
#         row, column = move
#         self.board[row][column] = self.current_player + 1
#
#     def switch_players(self):
#         self.current_player = (self.current_player + 1) % 2
#
#     def send_update(self):
#         for client_socket in self.client_connections:
#             self.send_message(client_socket, self.board)
#             self.send_message(client_socket, self.current_player)
#
#     def check_win(self):
#         win = False
#         for i in range(6):
#             if all(self.board[i][j] == self.current_player + 1 for j in range(6)):
#                 win = True
#                 break
#             if all(self.board[j][i] == self.current_player + 1 for j in range(6)):
#                 win = True
#                 break
#
#         if all(self.board[i][i] == self.current_player + 1 for i in range(6)):
#             win = True
#         if all(self.board[i][5 - i] == self.current_player + 1 for i in range(6)):
#             win = True
#
#         if win:
#             self.game_over = True
#
#     def check_game_over(self):
#         if all(all(row) for row in self.board):
#             self.game_over = True
#
#     def run_game_loop(self):
#         while True:
#             if not self.game_over:
#                 client_socket = self.client_connections[self.current_player]
#                 self.handle_move(client_socket)
#                 self.check_win()
#                 self.check_game_over()
#                 self.switch_players()
#                 self.send_update()
#
#             if self.game_over:
#                 self.server_socket.close()
#                 break
#
#
# if __name__ == "__main__":
#     server_address = ("localhost", 12345)
#     server = GameServer(server_address)
#     server.start()
#     server.run_game_loop()


import socket
import pickle
import threading

class GameServer:
    def __init__(self, server_address):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(server_address)
        self.clients = []
        self.boards = [[0 for _ in range(6)] for _ in range(6)]
        self.current_player = 0
        self.game_over = False

    def start(self):
        self.server_socket.listen(2)
        print("Serwer nasłuchuje na", self.server_socket.getsockname())

    def handle_client(self, client_socket, client_address, player_id):
        print("Gracz", player_id, "dołączył z adresu", client_address)
        self.clients.append((client_socket, player_id))

        while True:
            try:
                if self.game_over:
                    # Jeśli gra się skończyła, wyślij sygnał o zakończeniu gry do klienta
                    send_message(client_socket, "QUIT")
                    client_socket.close()
                    break

                # Odbierz ruch od klienta
                message = receive_message(client_socket)
                if message == "QUIT":
                    # Jeśli klient wysłał sygnał o zakończeniu gry, zamknij połączenie z klientem
                    client_socket.close()
                    break

                # Aktualizuj planszę na serwerze na podstawie otrzymanego ruchu
                row, column = message
                self.boards[row][column] = player_id + 1

                # Sprawdź, czy gracz wygrał
                win = False
                if all(self.boards[row][c] == player_id + 1 for c in range(6)):
                    win = True
                if all(self.boards[r][column] == player_id + 1 for r in range(6)):
                    win = True
                if row == column and all(self.boards[i][i] == player_id + 1 for i in range(6)):
                    win = True
                if row + column == 5 and all(self.boards[i][5 - i] == player_id + 1 for i in range(6)):
                    win = True

                if win:
                    # Jeśli gracz wygrał, wyślij sygnał o zakończeniu gry do klienta
                    send_message(client_socket, "QUIT")
                    client_socket.close()
                    self.game_over = True
                    break

                # Wyślij zaktualizowaną planszę do obu klientów
                for client in self.clients:
                    send_message(client[0], self.boards)

                # Zmiana gracza
                self.current_player = (self.current_player + 1) % 2

            except (ConnectionResetError, EOFError):
                # Jeśli wystąpił błąd połączenia, usuń klienta z listy i zakończ wątek
                print("Gracz", player_id, "rozłączony.")
                self.clients.remove((client_socket, player_id))
                client_socket.close()
                break

def send_message(client_socket, message):
    client_socket.sendall(pickle.dumps(message))

def receive_message(client_socket):
    data = client_socket.recv(4096)
    return pickle.loads(data)

# Inicjalizacja serwera
server_address = ("localhost", 12345)
game_server = GameServer(server_address)
game_server.start()

while len(game_server.clients) < 2:
    # Oczekuj na dołączenie dwóch graczy
    client_socket, client_address = game_server.server_socket.accept()
    player_id = len(game_server.clients)
    threading.Thread(target=game_server.handle_client, args=(client_socket, client_address, player_id)).start()
