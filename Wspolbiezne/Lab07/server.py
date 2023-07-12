import socket

SERVER_IP = 'localhost'
SERVER_PORT = 1000
BUFFER_SIZE = 1024


def get_game_result(player1_choice, player2_choice):
    if player1_choice == 'koniec' or player2_choice == 'koniec':
        return 'koniec'

    win_conditions = [('p', 'k'), ('k', 'n'), ('n', 'p')]

    if player1_choice == player2_choice:
        return 'tie'
    elif (player1_choice, player2_choice) in win_conditions:
        return 'win'
    else:
        return 'lose'


def play_game():
    player1_score = 0
    player2_score = 0

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((SERVER_IP, SERVER_PORT))

    while True:
        player1_choice, player1_addr = sock.recvfrom(BUFFER_SIZE)
        player2_choice, player2_addr = sock.recvfrom(BUFFER_SIZE)

        result = get_game_result(player1_choice.decode(), player2_choice.decode())
        result2 = get_game_result(player2_choice.decode(), player1_choice.decode())

        if result == 'win':
            player1_score += 1
        elif result == 'lose':
            player2_score += 1

        sock.sendto(f'{player2_choice.decode()},{result}'.encode(), player1_addr)
        sock.sendto(f'{player1_choice.decode()},{result2}'.encode(), player2_addr)

        if result == 'koniec':
            print('Koniec gry')
            print("Resetowanie wyników")
            break
        print(
            f'Gracz 1 ({player1_addr[0]}:{player1_addr[1]}): {player1_choice.decode()}\n'
            f'Gracz 2 ({player2_addr[0]}:{player2_addr[1]}): {player2_choice.decode()}\n'
            f'Wynik rundy:\n'
            f'Gracz 1:{result.upper()} Punkty:{player1_score}\n'
            f'Gracz 2:{result2.upper()} Punkty:{player2_score}\n')


if __name__ == '__main__':
    while True:
        try:
            play_game()
        except KeyboardInterrupt:
            break
