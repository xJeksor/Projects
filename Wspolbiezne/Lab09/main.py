import threading
import math
import time

mutex = threading.Lock()

num_threads = int(input("Podaj liczbę watków: "))

start_range = 1
end_range = 1_000_000

prime_numbers = []

barrier = threading.Barrier(num_threads + 1)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def thread_function(start, end):
    local_primes = []
    for num in range(start, end):
        if is_prime(num):
            local_primes.append(num)
    mutex.acquire()
    prime_numbers.extend(local_primes)
    mutex.release()

    barrier.wait()


threads = []
chunk_size = (end_range - start_range) // num_threads
start_time = time.time()
for i in range(num_threads):
    start = start_range + i * chunk_size
    end = start_range + (i + 1) * chunk_size
    thread = threading.Thread(target=thread_function, args=(start, end))
    threads.append(thread)
    thread.start()



barrier.wait()

end_time = time.time()

time = end_time - start_time
print("Czas wykonania: ", time, "sekund")

# Podaj liczbę watków: 1
# Czas wykonania:  1.9139153957366943 sekund

# Podaj liczbę watków: 10
# Czas wykonania:  0.9198360443115234 sekund

# Podaj liczbę watków: 100
# Czas wykonania:  0.026961326599121094 sekund

# Podaj liczbę watków: 1000
# Czas wykonania:  0.0010023117065429688 sekund
