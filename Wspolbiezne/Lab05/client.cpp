#include <iostream>
#include <cstring>
#include <cstdlib>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>

#define MAX_MSG_SIZE 1024

// Struktura reprezentująca pojedynczy komunikat w kolejce
struct Message {
    long type; // Typ komunikatu (PID klienta)
    char data[MAX_MSG_SIZE]; // Dane (zapytanie lub odpowiedź)
};

int main() {
    // Pobranie identyfikatora procesu
    pid_t pid = getpid();

    // Tworzenie kolejek komunikatów
    key_t input_queue_key = ftok(".", 'i');
    if (input_queue_key == -1) {
        perror("ftok");
        exit(EXIT_FAILURE);
    }
    int input_queue_id = msgget(input_queue_key, 0666);
    if (input_queue_id == -1) {
        perror("msgget");
        exit(EXIT_FAILURE);
    }

    key_t response_queue_key = ftok(".", 'o');
    if (response_queue_key == -1) {
        perror("ftok");
        exit(EXIT_FAILURE);
    }
    int response_queue_id = msgget(response_queue_key, 0666);
    if (response_queue_id == -1) {
        perror("msgget");
        exit(EXIT_FAILURE);
    }

    // Wysłanie zapytania do serwera
    Message request;
    request.type = pid;
    std::cout << "Podaj słowo po polsku: ";
    std::cin >> request.data;
    if (msgsnd(input_queue_id, &request, sizeof(Message) - sizeof(long), 0) == -1) {
        perror("msgsnd");
        exit(EXIT_FAILURE);
    }

    // Odczytanie odpowiedzi od serwera
    Message response;
    if (msgrcv(response_queue_id, &response, sizeof(Message) - sizeof(long), pid, 0) == -1) {
        perror("msgrcv");
        exit(EXIT_FAILURE);
    }

    std::cout << "Tłumaczenie: " << response.data << std::endl;

    return 0;
}
