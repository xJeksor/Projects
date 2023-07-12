# # # # # # # import pygame
# # # # # # # import socket
# # # # # # # import pickle
# # # # # # #
# # # # # # # # Inicjalizacja Pygame
# # # # # # # pygame.init()
# # # # # # #
# # # # # # # # Ustawienia okna gry
# # # # # # # WIDTH, HEIGHT = 600, 600
# # # # # # # BG_COLOR = (255, 255, 255)
# # # # # # # LINE_COLOR = (0, 0, 0)
# # # # # # # SQUARE_SIZE = 100
# # # # # # #
# # # # # # # # Inicjalizacja połączenia socket
# # # # # # # HOST = 'localhost'
# # # # # # # PORT = 12345
# # # # # # # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # # # # # # client_socket.connect((HOST, PORT))
# # # # # # #
# # # # # # # # Klasa GameClient
# # # # # # # class GameClient:
# # # # # # #     def __init__(self):
# # # # # # #         self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # #         pygame.display.set_caption("Gra Klient")
# # # # # # #
# # # # # # #         self.board = [[None for _ in range(6)] for _ in range(6)]
# # # # # # #         self.turn = None
# # # # # # #
# # # # # # #     def send_message(self, message):
# # # # # # #         client_socket.send(pickle.dumps(message))
# # # # # # #
# # # # # # #     def receive_message(self):
# # # # # # #         return pickle.loads(client_socket.recv(4096))
# # # # # # #
# # # # # # #     def draw_board(self):
# # # # # # #         if self.board is None:
# # # # # # #             return
# # # # # # #         self.screen.fill(BG_COLOR)
# # # # # # #
# # # # # # #         for row in range(6):
# # # # # # #             for col in range(6):
# # # # # # #                 pygame.draw.rect(self.screen, LINE_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
# # # # # # #                 if self.board[row][col] is not None:
# # # # # # #                     pygame.draw.rect(self.screen, self.board[row][col], (col * SQUARE_SIZE + 1, row * SQUARE_SIZE + 1, SQUARE_SIZE - 1, SQUARE_SIZE - 1))
# # # # # # #
# # # # # # #         pygame.display.update()
# # # # # # #
# # # # # # #     def handle_events(self):
# # # # # # #         for event in pygame.event.get():
# # # # # # #             if event.type == pygame.QUIT:
# # # # # # #                 pygame.quit()
# # # # # # #                 client_socket.close()
# # # # # # #                 exit()
# # # # # # #             elif event.type == pygame.MOUSEBUTTONDOWN and self.turn:
# # # # # # #                 x, y = pygame.mouse.get_pos()
# # # # # # #                 row = y // SQUARE_SIZE
# # # # # # #                 col = x // SQUARE_SIZE
# # # # # # #                 if self.board[row][col] is None:
# # # # # # #                     self.send_message((row, col))
# # # # # # #
# # # # # # #     def run(self):
# # # # # # #         self.turn = self.receive_message()
# # # # # # #         print("Initial Turn:", self.turn)
# # # # # # #
# # # # # # #         while True:
# # # # # # #             print("Waiting for events...")
# # # # # # #             for event in pygame.event.get():
# # # # # # #                 print("Event:", event)
# # # # # # #                 if event.type == pygame.QUIT:
# # # # # # #                     pygame.quit()
# # # # # # #                     client_socket.close()
# # # # # # #                     exit()
# # # # # # #
# # # # # # #             if self.turn:
# # # # # # #                 self.handle_events()
# # # # # # #
# # # # # # #             print("Requesting board...")
# # # # # # #             self.send_message("get_board")
# # # # # # #             self.board = self.receive_message()
# # # # # # #             print("Received board:", self.board)
# # # # # # #             self.draw_board()
# # # # # # #             self.turn = self.receive_message()
# # # # # # #             print("Turn:", self.turn)
# # # # # # #
# # # # # # #
# # # # # # # # Uruchomienie klienta
# # # # # # # if __name__ == '__main__':
# # # # # # #     game_client = GameClient()
# # # # # # #     game_client.run()
# # # # # # import numpy as np
# # # # # # import pygame
# # # # # # import socket
# # # # # # import pickle
# # # # # #
# # Inicjalizacja Pygame
# pygame.init()
#
# # Ustawienia okna gry
# WIDTH, HEIGHT = 600, 600
# BG_COLOR = (255, 255, 255)
# LINE_COLOR = (0, 0, 0)
# SQUARE_SIZE = 100
#
# # Inicjalizacja połączenia socket
# HOST = 'localhost'
# PORT = 12345
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((HOST, PORT))
#
# # Klasa GameClient
# class GameClient:
#     def __init__(self):
#         self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
#         pygame.display.set_caption("Gra Klient")
#
#         # self.board = [[None for _ in range(6)] for _ in range(6)]
#         self.board = np.zeros((6, 6), dtype=object)
#         self.turn = None
#
#     def send_message(self, message):
#         client_socket.send(pickle.dumps(message))
#
#     # def receive_message(self):
#     #     return pickle.loads(client_socket.recv(4096))
#
#     def receive_message(self):
#         data = client_socket.recv(4096)
#         if not data:
#             return None
#         return pickle.loads(data)
#
#     # def receive_message(self):
#     #     try:
#     #         data = pickle.loads(self.client_socket.recv(4096))
#     #         print("Received data:", data)
#     #         return data
#     #     except Exception as e:
#     #         print("Error receiving message:", e)
#     #         return None
#
#     # def receive_message(self, conn):
#     #     try:
#     #         data = conn.recv(4096)
#     #         if not data:
#     #             return None
#     #         message = pickle.loads(data)
#     #         print("Received message:", message)
#     #         return message
#     #     except Exception as e:
#     #         print("Error receiving message:", e)
#     #         return None
#
#     def draw_board(self):
#         if self.board is None:
#             return
#         self.screen.fill(BG_COLOR)
#
#         for row in range(6):
#             for col in range(6):
#                 pygame.draw.rect(self.screen, LINE_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
#                 # if self.board[row][col] == 0:
#                 pygame.draw.rect(
#                     self.screen,
#                         # self.board[row][col],
#                     (139, 69, 19),
#                     (
#                             col * SQUARE_SIZE + 1,
#                             row * SQUARE_SIZE + 1,
#                             SQUARE_SIZE - 1,
#                             SQUARE_SIZE - 1)
#                     )
#
#         pygame.display.update()
#
#     def handle_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 client_socket.close()
#                 exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN and self.turn:
#                 x, y = pygame.mouse.get_pos()
#                 row = y // SQUARE_SIZE
#                 col = x // SQUARE_SIZE
#                 if self.board[row][col] is None:
#                     self.send_message((row, col))
#
#     def run(self):
#         self.turn = self.receive_message()
#         print("Initial Turn:", self.turn)
#
#         while True:
#             self.handle_events()
#
#             self.send_message("get_board")
#             self.board = self.receive_message()
#             self.draw_board()
#             self.turn = self.receive_message()
#
#
# # Uruchomienie klienta
# if __name__ == '__main__':
#     game_client = GameClient()
#     game_client.run()
#

# # # # # import numpy as np
# # # # # import pygame
# # # # # import socket
# # # # # import pickle
# # # # #
# # # # # # Inicjalizacja Pygame
# # # # # pygame.init()
# # # # #
# # # # # # Ustawienia okna gry
# # # # # WIDTH, HEIGHT = 600, 600
# # # # # BG_COLOR = (255, 255, 255)
# # # # # LINE_COLOR = (0, 0, 0)
# # # # # SQUARE_SIZE = 100
# # # # #
# # # # # # Inicjalizacja połączenia socket
# # # # # HOST = 'localhost'
# # # # # PORT = 12345
# # # # # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # # # # client_socket.connect((HOST, PORT))
# # # # #
# # # # # # Klasa GameClient
# # # # # class GameClient:
# # # # #     def __init__(self):
# # # # #         self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # #         pygame.display.set_caption("Gra Klient")
# # # # #
# # # # #         self.board = [[None for _ in range(6)] for _ in range(6)]
# # # # #         # self.board = np.zeros((6, 6), dtype=object)
# # # # #         self.turn = None
# # # # #
# # # # #
# # # # #     def send_message(self, message):
# # # # #         client_socket.send(pickle.dumps(message))
# # # # #
# # # # #     def receive_message(self):
# # # # #         data = client_socket.recv(4096)
# # # # #         if not data:
# # # # #             return None
# # # # #         return pickle.loads(data)
# # # # #
# # # # #     def draw_board(self):
# # # # #         if self.board is None:
# # # # #             return
# # # # #         self.screen.fill(BG_COLOR)
# # # # #
# # # # #         for row in range(6):
# # # # #             for col in range(6):
# # # # #                 pygame.draw.rect(self.screen, LINE_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
# # # # #                 pygame.draw.rect(
# # # # #                     self.screen,
# # # # #                     # (139, 69, 19),
# # # # #                     self.board[row][col] or BG_COLOR,
# # # # #                     (
# # # # #                         col * SQUARE_SIZE + 1,
# # # # #                         row * SQUARE_SIZE + 1,
# # # # #                         SQUARE_SIZE - 1,
# # # # #                         SQUARE_SIZE - 1)
# # # # #                 )
# # # # #
# # # # #         pygame.display.update()
# # # # #
# # # # #     def handle_events(self):
# # # # #         for event in pygame.event.get():
# # # # #             if event.type == pygame.QUIT:
# # # # #                 pygame.quit()
# # # # #                 client_socket.close()
# # # # #                 exit()
# # # # #             elif event.type == pygame.MOUSEBUTTONDOWN and self.turn:
# # # # #                 x, y = pygame.mouse.get_pos()
# # # # #                 row = y // SQUARE_SIZE
# # # # #                 col = x // SQUARE_SIZE
# # # # #                 if self.board[row][col] is None and self.turn:
# # # # #                     self.send_message((row, col))
# # # # #
# # # # #     def run(self):
# # # # #         self.turn = self.receive_message()
# # # # #         print("Initial Turn:", self.turn)
# # # # #
# # # # #         while True:
# # # # #             self.handle_events()
# # # # #
# # # # #             self.send_message(self.turn)
# # # # #             self.board = self.receive_message()
# # # # #             self.draw_board()
# # # # #             self.turn = self.receive_message()
# # # # #
# # # # #
# # # # # # Uruchomienie klienta
# # # # # if __name__ == '__main__':
# # # # #     game_client = GameClient()
# # # # #     game_client.run()
# # # #
# # # # import pygame
# # # # import sys
# # # #
# # # # # Inicjalizacja Pygame
# # # # pygame.init()
# # # #
# # # # # Ustalenie rozmiaru planszy
# # # # board_size = (600, 600)
# # # # cell_size = 100
# # # #
# # # # # Ustalenie kolorów graczy
# # # # player_colors = [(255, 0, 0), (0, 255, 0)]  # Kolor gracza 1 (czerwony), Kolor gracza 2 (zielony)
# # # #
# # # # # Inicjalizacja planszy
# # # # board = [[0 for _ in range(6)] for _ in range(6)]
# # # #
# # # # # Inicjalizacja zmiennych gry
# # # # current_player = 0
# # # # game_over = False
# # # #
# # # # # Inicjalizacja ekranu Pygame
# # # # screen = pygame.display.set_mode(board_size)
# # # # pygame.display.set_caption("Gra Plansza")
# # # #
# # # # # Główna pętla gry
# # # # while not game_over:
# # # #     for event in pygame.event.get():
# # # #         if event.type == pygame.QUIT:
# # # #             pygame.quit()
# # # #             sys.exit()
# # # #
# # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # #             if not game_over:
# # # #                 # Pobierz pozycję kliknięcia myszą
# # # #                 mouse_pos = pygame.mouse.get_pos()
# # # #                 column = mouse_pos[0] // cell_size
# # # #                 row = mouse_pos[1] // cell_size
# # # #
# # # #                 # Sprawdź, czy pole jest puste
# # # #                 if board[row][column] == 0:
# # # #                     # Zamaluj pole na planszy
# # # #                     board[row][column] = current_player + 1
# # # #
# # # #                     # Sprawdź, czy gracz wygrał
# # # #                     win = False
# # # #                     # Sprawdź wiersze
# # # #                     if all(board[row][c] == current_player + 1 for c in range(6)):
# # # #                         win = True
# # # #                     # Sprawdź kolumny
# # # #                     if all(board[r][column] == current_player + 1 for r in range(6)):
# # # #                         win = True
# # # #                     # Sprawdź przekątne
# # # #                     if row == column and all(board[i][i] == current_player + 1 for i in range(6)):
# # # #                         win = True
# # # #                     if row + column == 5 and all(board[i][5 - i] == current_player + 1 for i in range(6)):
# # # #                         win = True
# # # #
# # # #                     # Zmiana gracza, jeśli nie ma wygranej
# # # #                     if not win:
# # # #                         current_player = (current_player + 1) % 2
# # # #
# # # #                     # Sprawdź, czy plansza jest pełna
# # # #                     if all(all(row) for row in board):
# # # #                         game_over = True
# # # #
# # # #     # Wypełnij ekran kolorem tła
# # # #     screen.fill((255, 255, 255))
# # # #
# # # #     # Rysuj planszę
# # # #     for row in range(6):
# # # #         for column in range(6):
# # # #             cell_color = player_colors[board[row][column] - 1] if board[row][column] != 0 else (200, 200, 200)
# # # #             pygame.draw.rect(screen, cell_color, (column * cell_size, row * cell_size, cell_size, cell_size))
# # # #
# # # #     # Wyświetl aktualny stan planszy
# # # #     pygame.display.flip()
# # # #
# # # # # Oblicz punkty
# # # # scores = [0, 0]
# # # # for row in range(6):
# # # #     scores[0] += board[row].count(1)
# # # #     scores[1] += board[row].count(2)
# # # #
# # # # # Wyświetl wynik
# # # # print("Koniec gry!")
# # # # print("Gracz 1 zdobył", scores[0], "punktów.")
# # # # print("Gracz 2 zdobył", scores[1], "punktów.")
# # # # if scores[0] > scores[1]:
# # # #     print("Gracz 1 wygrał!")
# # # # elif scores[1] > scores[0]:
# # # #     print("Gracz 2 wygrał!")
# # # # else:
# # # #     print("Remis!")
# # # import pygame
# # # import sys
# # # import socket
# # # import pickle
# # #
# # # # Inicjalizacja Pygame
# # # pygame.init()
# # #
# # # # Ustalenie rozmiaru planszy
# # # board_size = (600, 600)
# # # cell_size = 100
# # #
# # # # Ustalenie kolorów graczy
# # # player_colors = [(255, 0, 0), (0, 255, 0)]  # Kolor gracza 1 (czerwony), Kolor gracza 2 (zielony)
# # #
# # # # Inicjalizacja planszy
# # # board = [[0 for _ in range(6)] for _ in range(6)]
# # #
# # # # Inicjalizacja zmiennych gry
# # # current_player = 0
# # # game_over = False
# # #
# # # # Inicjalizacja ekranu Pygame
# # # screen = pygame.display.set_mode(board_size)
# # # pygame.display.set_caption("Gra Plansza")
# # #
# # #
# # # class GameClient:
# # #     def __init__(self):
# # #         self.server_address = ('localhost', 5555)  # Adres serwera
# # #         self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # #         self.player_number = None  # Numer przypisany graczowi
# # #         self.game_over = False
# # #
# # #     def connect_to_server(self):
# # #         self.client_socket.connect(self.server_address)
# # #         self.player_number = pickle.loads(self.client_socket.recv(1024))
# # #         print("Podłączono do serwera. Jesteś graczem", self.player_number)
# # #
# # #     def send_message(self, message):
# # #         self.client_socket.send(pickle.dumps(message))
# # #
# # #     def receive_update(self):
# # #         data = pickle.loads(self.client_socket.recv(1024))
# # #         self.game_over = data['game_over']
# # #         self.board = data['board']
# # #         self.current_player = data['current_player']
# # #
# # #     def draw_board(self):
# # #         for row in range(6):
# # #             for column in range(6):
# # #                 cell_color = player_colors[self.board[row][column] - 1] if self.board[row][column] != 0 else (200, 200, 200)
# # #                 pygame.draw.rect(screen, cell_color, (column * cell_size, row * cell_size, cell_size, cell_size))
# # #
# # #         # Wyświetl aktualny stan planszy
# # #         pygame.display.flip()
# # #
# # #
# # # # Inicjalizacja klienta gry
# # # game_client = GameClient()
# # # game_client.connect_to_server()
# # #
# # # # Główna pętla gry
# # # while not game_client.game_over:
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             pygame.quit()
# # #             sys.exit()
# # #
# # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # #             if not game_client.game_over:
# # #                 # Pobierz pozycję kliknięcia myszą
# # #                 mouse_pos = pygame.mouse.get_pos()
# # #                 column = mouse_pos[0] // cell_size
# # #                 row = mouse_pos[1] // cell_size
# # #
# # #                 # Sprawdź, czy pole jest puste
# # #                 if game_client.board[row][column] == 0 and game_client.current_player == game_client.player_number - 1:
# # #                     # Wyślij ruch do serwera
# # #                     game_client.send_message({'player_number': game_client.player_number, 'row': row, 'column': column})
# # #
# # #     # Pobierz aktualizację od serwera
# # #     game_client.receive_update()
# # #
# # #     # Wypełnij ekran kolorem tła
# # #     screen.fill((255, 255, 255))
# # #
# # #     # Rysuj planszę
# # #     game_client.draw_board()
# # #
# # # # Oblicz punkty
# # # scores = [0, 0]
# # # for row in range(6):
# # #     scores[0] += game_client.board[row].count(1)
# # #     scores[1] += game_client.board[row].count(2)
# # #
# # # # Wyświetl wynik
# # # print("Koniec gry!")
# # # print("Gracz 1 zdobył", scores[0], "punktów.")
# # # print("Gracz 2 zdobył", scores[1], "punktów.")
# # # if scores[0] > scores[1]:
# # #     print("Gracz 1 wygrał!")
# # # elif scores[1] > scores[0]:
# # #     print("Gracz 2 wygrał!")
# # # else:
# # #     print("Remis!")
# #
# #
# # import pygame
# # import sys
# # import socket
# # import pickle
# #
# # # Inicjalizacja Pygame
# # pygame.init()
# #
# # # Ustalenie rozmiaru planszy
# # board_size = (600, 600)
# # cell_size = 100
# #
# # # Ustalenie kolorów graczy
# # player_colors = [(255, 0, 0), (0, 255, 0)]  # Kolor gracza 1 (czerwony), Kolor gracza 2 (zielony)
# #
# # # Inicjalizacja ekranu Pygame
# # screen = pygame.display.set_mode(board_size)
# # pygame.display.set_caption("Gra Plansza")
# #
# # # Klasa GameClient
# # class GameClient:
# #     def __init__(self, server_address):
# #         self.server_address = server_address
# #         self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #         self.board = None
# #         self.current_player = None
# #         self.game_over = False
# #
# #     def connect(self):
# #         self.client_socket.connect(self.server_address)
# #
# #     def send_message(self, message):
# #         self.client_socket.sendall(pickle.dumps(message))
# #
# #     def receive_message(self):
# #         data = self.client_socket.recv(1024)
# #         return pickle.loads(data)
# #
# #     def start(self):
# #         self.connect()
# #         self.setup_game()
# #
# #     def setup_game(self):
# #         self.board = self.receive_message()
# #         self.current_player = self.receive_message()
# #
# #     def handle_click(self, row, column):
# #         if not self.game_over and self.current_player is not None:
# #             if self.board[row][column] == 0:
# #                 self.board[row][column] = self.current_player + 1
# #                 self.send_message((row, column))
# #
# #                 self.check_win()
# #                 self.check_game_over()
# #                 self.switch_players()
# #
# #     def check_win(self):
# #         win = False
# #         for i in range(6):
# #             if all(self.board[i][j] == self.current_player + 1 for j in range(6)):
# #                 win = True
# #                 break
# #             if all(self.board[j][i] == self.current_player + 1 for j in range(6)):
# #                 win = True
# #                 break
# #
# #         if all(self.board[i][i] == self.current_player + 1 for i in range(6)):
# #             win = True
# #         if all(self.board[i][5 - i] == self.current_player + 1 for i in range(6)):
# #             win = True
# #
# #         if win:
# #             self.game_over = True
# #
# #     def check_game_over(self):
# #         if all(all(row) for row in self.board):
# #             self.game_over = True
# #
# #     def switch_players(self):
# #         self.current_player = (self.current_player + 1) % 2
# #
# #     def draw_board(self):
# #         screen.fill((255, 255, 255))
# #
# #         for row in range(6):
# #             for column in range(6):
# #                 cell_color = player_colors[self.board[row][column] - 1] if self.board[row][column] != 0 else (200, 200, 200)
# #                 pygame.draw.rect(screen, cell_color, (column * cell_size, row * cell_size, cell_size, cell_size))
# #
# #         pygame.display.flip()
# #
# #     def run_game_loop(self):
# #         while True:
# #             for event in pygame.event.get():
# #                 if event.type == pygame.QUIT:
# #                     self.client_socket.close()
# #                     pygame.quit()
# #                     sys.exit()
# #
# #                 if event.type == pygame.MOUSEBUTTONDOWN:
# #                     if not self.game_over:
# #                         mouse_pos = pygame.mouse.get_pos()
# #                         column = mouse_pos[0] // cell_size
# #                         row = mouse_pos[1] // cell_size
# #                         self.handle_click(row, column)
# #
# #             self.draw_board()
# #             pygame.time.wait(100)
# #
# #
# # if __name__ == "__main__":
# #     server_address = ("localhost", 12345)
# #     client = GameClient(server_address)
# #     client.start()
# #     client.run_game_loop()
#
# import pygame
# import sys
# import pickle
# import socket
#
# # Inicjalizacja Pygame
# pygame.init()
#
# # Ustalenie rozmiaru planszy
# board_size = (600, 600)
# cell_size = 100
#
# # Ustalenie kolorów graczy
# player_colors = [(255, 0, 0), (0, 255, 0)]  # Kolor gracza 1 (czerwony), Kolor gracza 2 (zielony)
#
# # Inicjalizacja planszy
# board = [[0 for _ in range(6)] for _ in range(6)]
#
# # Inicjalizacja zmiennych gry
# current_player = 0
# game_over = False
#
# # Inicjalizacja ekranu Pygame
# screen = pygame.display.set_mode(board_size)
# pygame.display.set_caption("Gra Plansza")
#
# # Inicjalizacja połączenia z serwerem
# server_address = ("localhost", 12345)
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(server_address)
#
# # Funkcja do wysyłania wiadomości do serwera
# def send_message(message):
#     client_socket.sendall(pickle.dumps(message))
#
# # Funkcja do odbierania wiadomości od serwera
# def receive_message():
#     data = client_socket.recv(1024)
#     return pickle.loads(data)
#
# # Funkcja do obsługi kliknięcia myszą
# def handle_click(row, column):
#     global current_player, game_over
#
#     if not game_over:
#         if board[row][column] == 0:
#             board[row][column] = current_player + 1
#             send_message((row, column))  # Wysłanie ruchu do serwera
#
#             # Sprawdź, czy gracz wygrał
#             win = False
#             if all(board[row][c] == current_player + 1 for c in range(6)):
#                 win = True
#             if all(board[r][column] == current_player + 1 for r in range(6)):
#                 win = True
#             if row == column and all(board[i][i] == current_player + 1 for i in range(6)):
#                 win = True
#             if row + column == 5 and all(board[i][5 - i] == current_player + 1 for i in range(6)):
#                 win = True
#
#             # Zmiana gracza, jeśli nie ma wygranej
#             if not win:
#                 current_player = (current_player + 1) % 2
#
#             # Sprawdź, czy plansza jest pełna
#             if all(all(row) for row in board):
#                 game_over = True
#
# # Główna pętla gry
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             send_message("QUIT")  # Wysłanie sygnału do serwera o zakończeniu gry
#             client_socket.close()
#             pygame.quit()
#             sys.exit()
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if not game_over:
#                 mouse_pos = pygame.mouse.get_pos()
#                 column = mouse_pos[0] // cell_size
#                 row = mouse_pos[1] // cell_size
#                 handle_click(row, column)
#
#     # Wypełnij ekran kolorem tła
#     screen.fill((255, 255, 255))
#
#     # Rysuj planszę
#     for row in range(6):
#         for column in range(6):
#             cell_color = player_colors[board[row][column] - 1] if board[row][column] != 0 else (200, 200, 200)
#             pygame.draw.rect(screen, cell_color, (column * cell_size, row * cell_size, cell_size, cell_size))
#
#     # Wyświetl aktualny stan planszy
#     pygame.display.flip()
#
#     # Odbierz wiadomość od serwera
#     message = receive_message()
#
#     if message == "QUIT":
#         # Jeśli otrzymaliśmy sygnał o zakończeniu gry, zamknij połączenie i wyjdź z pętli
#         client_socket.close()
#         break
#
#     # Aktualizuj planszę na podstawie otrzymanej wiadomości od serwera
#     board = message
#
#     # Aktualizuj zmienną game_over na podstawie stanu planszy
#     game_over = all(all(row) for row in board)
#
# # Oblicz punkty
# scores = [0, 0]
# for row in range(6):
#     scores[0] += board[row].count(1)
#     scores[1] += board[row].count(2)
#
# # Wyświetl wynik
# print("Koniec gry!")
# print("Gracz 1 zdobył", scores[0], "punktów.")
# print("Gracz 2 zdobył", scores[1], "punktów.")
# if scores[0] > scores[1]:
#     print("Gracz 1 wygrał!")
# elif scores[1] > scores[0]:
#     print("Gracz 2 wygrał!")
# else:
#     print("Remis!")

import pygame
import socket
import pickle

class GameClient:
    def __init__(self, server_address):
        self.server_address = server_address
        self.player_id = None
        self.board = [[0 for _ in range(6)] for _ in range(6)]
        self.current_player = 0
        self.game_over = False

        # Inicjalizacja połączenia socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.server_address)

        # Wysłanie żądania dołączenia do gry
        self.send_message("JOIN")

        # Odebranie identyfikatora gracza
        self.player_id = self.receive_message()

        # Inicjalizacja Pygame
        pygame.init()

        # Ustalenie rozmiaru planszy
        self.board_size = (600, 600)
        self.cell_size = 100

        # Ustalenie kolorów graczy
        self.player_colors = [(255, 0, 0), (0, 255, 0)]

        # Inicjalizacja ekranu Pygame
        self.screen = pygame.display.set_mode(self.board_size)
        pygame.display.set_caption("Gra Plansza")

    def send_message(self, message):
        self.client_socket.sendall(pickle.dumps(message))

    def receive_message(self):
        data = self.client_socket.recv(1024)
        return pickle.loads(data)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.send_message("QUIT")
                self.client_socket.close()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.game_over:
                    # Pobierz pozycję kliknięcia myszą
                    mouse_pos = pygame.mouse.get_pos()
                    column = mouse_pos[0] // self.cell_size
                    row = mouse_pos[1] // self.cell_size

                    # Sprawdź, czy pole jest puste
                    if self.board[row][column] == 0 and self.current_player == self.player_id:
                        # Zamaluj pole na planszy
                        self.board[row][column] = self.current_player + 1

                        # Wyślij ruch do serwera
                        self.send_message((row, column))

    def update_game_state(self):
        # Odbierz zaktualizowaną planszę od serwera
        self.board = self.receive_message()

        # Sprawdź, czy gra się zakończyła
        if self.board == "QUIT":
            self.game_over = True

        # Zmień gracza, jeśli gra nadal trwa
        if not self.game_over:
            self.current_player = (self.current_player + 1) % 2

    def draw_board(self):
        self.screen.fill((255, 255, 255))

        # Rysuj planszę
        for row in range(6):
            for column in range(6):
                cell_color = self.player_colors[self.board[row][column] - 1] if self.board[row][column] != 0 else (200, 200, 200)
                pygame.draw.rect(self.screen, cell_color, (column * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()

        while not self.game_over:
            clock.tick(60)

            self.handle_input()

            self.update_game_state()

            self.draw_board()

        pygame.quit()
        self.client_socket.close()

if __name__ == "__main__":
    server_address = ("localhost", 12345)  # Adres i port serwera
    game_client = GameClient(server_address)
    game_client.run()
