import threading
import numpy as np
import time


def sum_array_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left = sum_array_recursive(arr[:mid])
        right = sum_array_recursive(arr[mid:])
        return left + right


def split_array(arr, num_threads):
    chunk_size = len(arr) // num_threads
    chunks = []
    for i in range(0, len(arr), chunk_size):
        chunk = arr[i:i + chunk_size]
        chunks.append(chunk)
    return chunks


def sum_subarray(arr, result, mutex):
    subarray_sum = sum(arr)
    mutex.acquire()
    result.append(subarray_sum)
    mutex.release()


def multi_threaded_sum(arr, num_threads):
    result = []
    mutex = threading.Lock()
    threads = []

    chunks = split_array(arr, num_threads)

    for chunk in chunks:
        t = threading.Thread(target=sum_subarray, args=(chunk, result, mutex))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    total_sum = sum(result)
    return total_sum


def sum_subarray_recursive(arr, result, mutex):
    subarray_sum = sum_array_recursive(arr)
    mutex.acquire()
    result.append(subarray_sum)
    mutex.release()


def multi_threaded_sum_recursive(arr, num_threads):
    result = []
    mutex = threading.Lock()
    threads = []

    chunks = split_array(arr, num_threads)

    for chunk in chunks:
        t = threading.Thread(target=sum_subarray_recursive, args=(chunk, result, mutex))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    total_sum = sum(result)
    return total_sum


array = np.loadtxt('array.txt', delimiter=',')

if __name__ == "__main__":
    print("Iteracyjnie -> 1")
    print("Rekurencyjne -> 2")

    choice = int(input("Twoj wybór: "))

    if choice == 1:
        thread_number = int(input("Liczba wątków: "))
        t = time.process_time()
        result = multi_threaded_sum(array, thread_number)
        elapsed_time = time.process_time() - t
        print("Suma:", result)
        print("Czas wykonania: ", elapsed_time)
    elif choice == 2:
        thread_number = int(input("Podaj liczbę wątków: "))
        t = time.process_time()
        result = multi_threaded_sum_recursive(array, thread_number)
        elapsed_time = time.process_time() - t
        print("Suma:", result)
        print("Czas wykonania: ", elapsed_time)
