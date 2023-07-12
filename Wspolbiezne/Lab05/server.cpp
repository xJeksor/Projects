#include <iostream>
#include <cstring>
#include <cstdlib>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <unordered_map>

#define MAX_MSG_SIZE 1024

// Struktura reprezentująca pojedynczy komunikat w kolejce
struct Message {
    long type; // Typ komunikatu (PID klienta)
    char data[MAX_MSG_SIZE]; // Dane (zapytanie lub odpowiedź)
};

// Funkcja obsługująca zapytania klientów
void handle_request(Message request, int response_queue_id) {
    std::string word(request.data);

    // Przykładowa baza słów
    std::unordered_map<std::string, std::string> dictionary = {
        {"jabłko", "apple"},
        {"gruszka", "pear"},
        {"pomarańcza", "orange"}
    };

    // Szukanie odpowiedzi na podstawie zapytania
    std::string answer;
    if (dictionary.count(word)) {
        answer = dictionary[word];
    } else {
        answer = "Nie znam takiego słowa.";
    }

    // Wysłanie odpowiedzi do klienta
    Message response;
    response.type = request.type;
    std::strcpy(response.data, answer.c_str());
    if (msgsnd(response_queue_id, &response, sizeof(Message) - sizeof(long), 0) == -1) {
        perror("msgsnd");
        exit(EXIT_FAILURE);
    }
}

int main() {
    // Tworzenie kolejek komunikatów
    key_t input_queue_key = ftok(".", 'i');
    if (input_queue_key == -1) {
        perror("ftok");
        exit(EXIT_FAILURE);
    }
    int input_queue_id = msgget(input_queue_key, IPC_CREAT | 0666);
    if (input_queue_id == -1) {
        perror("msgget");
        exit(EXIT_FAILURE);
    }

    key_t response_queue_key = ftok(".", 'o');
    if (response_queue_key == -1) {
        perror("ftok");
        exit(EXIT_FAILURE);
    }
    int response_queue_id = msgget(response_queue_key, IPC_CREAT | 0666);
    if (response_queue_id == -1) {
        perror("msgget");
        exit(EXIT_FAILURE);
    }

    std::cout << "Serwer gotowy do obsługi klientów." << std::endl;

    // Pętla obsługująca zapytania klientów
    while (true) {
        // Odczytanie zapytania z kolejki wejściowej
        Message request;
        if (msgrcv(input_queue_id, &request, sizeof(Message) - sizeof(long), 0, 0) == -1) {
            perror("msgrcv");
            exit(EXIT_FAILURE);
        }

        // Obsługa zapytania
        handle_request(request, response_queue_id);
    }

    // Usunięcie kolejek komunikatów
    if (msgctl(input_queue_id, IPC_RMID, nullptr) == -1) {
        perror("msgctl");
        exit(EXIT_FAILURE);
    }
    if (msgctl(response_queue_id, IPC_RMID, nullptr) == -1) {
        perror("msgctl");
        exit(EXIT_FAILURE);
    }

    return 0;
}
