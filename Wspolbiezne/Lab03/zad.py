import os
import sys


def read_file(file_name, word_to_search):
    count = 0
    parameter_file_name = ""
    with open(file_name, 'r') as file:
        pid = -1
        for line in file:
            words = line.split()
            for word in words:
                if word.startswith("\\input{") and word.endswith('}'):
                    parameter_file_name = word[word.find('{') + 1: word.find('}')]
                    pid = os.fork()
                    if pid == -1:
                        print("Błąd przy tworzeniu procesu potomnego")
                        exit(0)
                    if pid > 0:
                        # parent process
                        continue
                    else:
                        # child process
                        file_name = parameter_file_name
                        count = read_file(file_name, word_to_search)
                        os._exit(count)

                # Jeśli zmienna pid jest większa niż 0, oznacza to, że program wykonuje się w
                # procesie rodzica. W takim przypadku blok if czeka na zakończenie procesu potomnego przy pomocy
                # funkcji os.wait(). Po zakończeniu procesu potomnego, sprawdza czy proces zakończył się poprawnie
                # przy pomocy funkcji os.WIFEXITED(), a następnie dodaje wynik działania procesu potomnego do
                # zmiennej count.
                if word.startswith(word_to_search):
                    count += 1
                    # wait for child process
                    if pid > 0:
                        _, status = os.wait()
                        if os.WIFEXITED(status):
                            count += os.WEXITSTATUS(status)
    return count


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Przykładowe wywołanie: python main.py nazwa_pliku slowo_do_wyszukania")
        exit(0)

    file_name = sys.argv[1]
    word_to_search = sys.argv[2]

    count = read_file(file_name, word_to_search)
    print(f"{count} znalezione wystąpienia podanego słowa")
