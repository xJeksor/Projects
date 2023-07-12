import socket

SERVER_IP = 'localhost'
SERVER_PORT = 1000
BUFFER_SIZE = 1024


def get_player_choice():
    while True:
        choice = input(
            'Papier -> p, Kamień -> k, Nożyce -> n, Koniec gry -> koniec: ').strip(
        ).lower()
        if choice in ('p', 'k', 'n', 'koniec'):
            return choice
        else:
            print('Wybierz poprawny wybór: p,k,n,koniec.')


def play_game():
    player_score = 0
    opponent_score = 0

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect((SERVER_IP, SERVER_PORT))
        while True:
            player_choice = get_player_choice()
            sock.send(player_choice.encode())

            server_choice, result = sock.recv(BUFFER_SIZE).decode().split(',')
            if result == 'win':
                player_score += 1
            elif result == 'lose':
                opponent_score += 1
            elif result == 'koniec':
                print('Koniec gry')
                break

            print(
                f'Twój wybór: {player_choice}\nWybór przeciwnika: {server_choice}\nWynik rundy: {result.upper()}'
            )
            print(
                f'Twoje punkty: {player_score}\nPunkty przeciwnika: {opponent_score}')
    except KeyboardInterrupt:
        pass
    finally:
        sock.close()


if __name__ == '__main__':
    play_game()
