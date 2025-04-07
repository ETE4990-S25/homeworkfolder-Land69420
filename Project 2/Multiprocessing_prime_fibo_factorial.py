import multiprocessing
import multiprocessing.process
import time

# large prime part of project
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, stepsize, result, time_limit):
    highest_prime = -1
    starttime = time.time()

    number = start

    while time.time() - starttime < time_limit:
        if is_prime(number):
            highest_prime = number
        number += stepsize

    result.append(highest_prime)


def highest_prime(time_limit, number_of_threads):
    """each thread will find if the n*number of threads + i number is prime where 
    n is the iteration and i will be range(0, number of threads)

    time limit is in seconds
    """

    print(f"finding largest prime in {time_limit} seconds.")
    
    manager = multiprocessing.Manager()
    shared_list = manager.list()

    Processes = [
        multiprocessing.Process(
            target = primes_in_range,
            args = (2*i+1 , number_of_threads * 2, shared_list, time_limit)
        )
        for i in range(number_of_threads)
    ]

    for p in Processes:
        p.start()
 

    for p in Processes:
        p.join()

    return max(shared_list) if shared_list else "failed"


# fibonacci part of project
def nth_fibo(n):
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b
    return b


# factorial part of project
def factorial_part(start, end, shared_result, lock):
    """this is ur code from lecture"""
    result = 1

    for i in range(start, end):
        result *= i

    with lock:
        shared_result.value *= result

def factorial(n, number_of_processes):
    range_per_process = n // number_of_processes
    shared_result = multiprocessing.Value('d', 1.0) 
    lock = multiprocessing.Lock()

    processes = [
        multiprocessing.Process(
            target=factorial_part, 
            args=(i * range_per_process + 1, (i + 1) * range_per_process + 1, shared_result, lock))
            for i in range(number_of_processes)
    ]


    for p in processes:
        p.start()
    for p in processes:
        p.join()

    return(shared_result.value)

if __name__ == "__main__":

    hp = highest_prime(time_limit= 1, number_of_threads= 10)
    print(hp)

    high_fibo = nth_fibo(10)
    print(high_fibo)

    high_factorial = factorial(10, 10)
    print(high_factorial)
