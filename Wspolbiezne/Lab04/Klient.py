import os
import sys
import struct
import time

class Person:
    def __init__(self, id, surname):
        self.id = id
        self.surname = surname

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <id> <client_fifo>")
        exit(1)

    client_id = int(sys.argv[1])
    client_fifo = sys.argv[2]
    os.mkfifo(client_fifo, 0o666)

    server_fifo = 'server_input_fifo'
    server_fd = os.open(server_fifo, os.O_WRONLY)

    # send request to server
    message = f"{client_id} {client_fifo}"
    os.write(server_fd, message.encode())
    os.close(server_fd)

    # read response from client queue
    client_fd = os.open(client_fifo, os.O_RDONLY)

    surname = os.read(client_fd, 20).decode().strip()
    os.close(client_fd)

    os.unlink(client_fifo)

    # print response
    if surname == 'None':
        print("ID not found in the database.")
    else:
        print(f"Surname: {surname}")

if __name__ == '__main__':
    main()
