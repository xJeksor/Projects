import pygame
import sys
import socket

# Inicjalizacja Pygame
pygame.init()

# Ustawienia planszy
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 6
SQUARE_SIZE = SCREEN_WIDTH // GRID_SIZE

# Ustawienia kolorów
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYER1_COLOR = (255, 0, 0)
PLAYER2_COLOR = (0, 0, 255)
SCORE_COLOR = (0, 255, 0)
filled_lines = []

# Inicjalizacja planszy
board = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]

# Inicjalizacja gracza
current_player = 1

# Inicjalizacja punktacji
player1_score = 0
player2_score = 0

# Inicjalizacja interfejsu graficznego
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gra w Ziemniaki")


# Funkcja sprawdzająca, czy dany ruch jest poprawny
def is_valid_move(row, col):
    return board[row][col] is None


# Funkcja sprawdzająca, czy gra została zakończona
def is_game_over():
    return all(all(square is not None for square in row) for row in board)


# Funkcja sprawdzająca, czy jest linia zakończona
def is_line_complete(line):
    return all(square is not None for square in line)


# Funkcja zliczająca punkty dla danego gracza
def count_points(line):
    return line.count(current_player)


# Funkcja aktualizująca punktację
def update_score(points):
    global player1_score, player2_score
    if current_player == 1:
        player1_score += points
    else:
        player2_score += points


# Funkcja rysująca planszę na ekranie
def draw_board():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            square_color = BLACK if board[row][col] is None else \
                PLAYER1_COLOR if board[row][col] == 1 else PLAYER2_COLOR
            pygame.draw.rect(screen, square_color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def draw_score():
    font = pygame.font.Font(None, 36)
    player1_score_text = font.render(f"Gracz 1: {player1_score}", True, SCORE_COLOR)
    player2_score_text = font.render(f"Gracz 2: {player2_score}", True, SCORE_COLOR)
    screen.blit(player1_score_text, (SCREEN_WIDTH // 2 - player1_score_text.get_width() // 2, 10))
    screen.blit(player2_score_text, (SCREEN_WIDTH // 2 - player2_score_text.get_width() // 2, 50))


while True:
    # Obsługa zdarzeń
    # Zapelnione linie
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not is_game_over():
                # Pobranie pozycji kliknięcia myszą
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Obliczenie indeksów kwadratu na planszy
                row = mouse_y // SQUARE_SIZE
                col = mouse_x // SQUARE_SIZE
                if is_valid_move(row, col):
                    # Aktualizacja planszy
                    board[row][col] = current_player
                    # Sprawdzenie linii pionowych
                    line = [board[i][col] for i in range(GRID_SIZE)]
                    if is_line_complete(line):
                        points = count_points(line)
                        update_score(points)

                    # Sprawdzenie linii poziomych
                    line = [board[row][i] for i in range(GRID_SIZE)]
                    if is_line_complete(line):
                        points = count_points(line)
                        update_score(points)

                    # Sprawdzenie linii skośnych
                    line = [board[i][i] for i in range(GRID_SIZE)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    line = [board[i + 1][i] for i in range(GRID_SIZE - 1)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    line = [board[i + 2][i] for i in range(GRID_SIZE - 2)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    line = [board[i + 3][i] for i in range(GRID_SIZE - 3)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    line = [board[i + 4][i] for i in range(GRID_SIZE - 4)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    line = [board[i][i + 1] for i in range(GRID_SIZE - 1)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    line = [board[i][i + 2] for i in range(GRID_SIZE - 2)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    line = [board[i][i + 3] for i in range(GRID_SIZE - 3)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    line = [board[i][i + 4] for i in range(GRID_SIZE - 4)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    # Druga przekatna

                    line = [board[1 - i][i] for i in range(GRID_SIZE - 4)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    line = [board[2 - i][i] for i in range(GRID_SIZE - 3)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    line = [board[3 - i][i] for i in range(GRID_SIZE - 2)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)
                    line = [board[4 - i][i] for i in range(GRID_SIZE - 1)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)
                    line = [board[5 - i][i] for i in range(GRID_SIZE)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    # Kolejna czesc
                    line = [board[i + 1][5 - i] for i in range(GRID_SIZE - 1)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    line = [board[i + 2][5 - i] for i in range(GRID_SIZE - 2)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    line = [board[i + 3][5 - i] for i in range(GRID_SIZE - 3)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)

                    line = [board[i + 4][5 - i] for i in range(GRID_SIZE - 4)]
                    if is_line_complete(line) and line not in filled_lines:
                        points = count_points(line)
                        update_score(points)
                        filled_lines.append(line)
                    # Zmiana aktualnego gracza
                    current_player = 2 if current_player == 1 else 1

    # Wyczyszczenie ekranu
    screen.fill(WHITE)

    # Rysowanie planszy i punktów
    draw_board()
    draw_score()

    # Aktualizacja ekranu
    pygame.display.flip()
