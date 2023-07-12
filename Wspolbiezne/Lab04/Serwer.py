import os
import signal
import struct

def handle_SIGTERM(signum, frame):
    print('Server terminated.')
    exit(0)

def handle_SIGUSR1(signum, frame):
    print('Server terminated by SIGUSR1 signal.')
    exit(0)

signal.signal(signal.SIGHUP, signal.SIG_IGN)
signal.signal(signal.SIGTERM, handle_SIGTERM)
signal.signal(signal.SIGUSR1, handle_SIGUSR1)

class Person:
    def __init__(self, id, surname):
        self.id = id
        self.surname = surname

database = [
    Person(1, 'Smith'),
    Person(2, 'Johnson'),
    Person(3, 'Williams'),
    Person(4, 'Jones'),
    Person(5, 'Tomek'),
]

def search_database(client_id):
    surname = 'None'
    for person in database:
        if person.id == client_id:
            surname = person.surname
            break
    return surname.encode()

def main():
    # create and open the input FIFO queue
    input_fifo = 'server_input_fifo'
    os.mkfifo(input_fifo, 0o666)
    input_fd = os.open(input_fifo, os.O_RDONLY)
    test_fd = os.open(input_fifo, os.O_WRONLY)

    # server loop
    while True:
        # read request from input queue
        message = os.read(input_fd, 40)
        if message:
            message = message.decode().strip()
            print(message)

            client_id, client_fifo = message.split(' ')
            client_id = int(client_id)

            # search for ID in the database
            surname = search_database(client_id)

            # send response to client queue
            response_fifo = client_fifo
            response_fd = os.open(response_fifo, os.O_WRONLY)
            os.write(response_fd, struct.pack('20s', surname))
            os.fsync(response_fd)  # flush output buffer
            os.close(response_fd)

    os.close(input_fd)

if __name__ == '__main__':
    main()
