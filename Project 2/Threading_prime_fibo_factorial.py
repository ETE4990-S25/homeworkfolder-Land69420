import threading
import time

# keeps the large numbers from breaking code
import sys
sys.set_int_max_str_digits(0)

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
    
    shared_result = [-1]

    threads = [
        threading.Thread(
            target = primes_in_range,
            args = (2*i+1 , number_of_threads * 2, shared_result, time_limit) # only checks odd numbers, splits threads by alternating which thread checks which number.
        )
        for i in range(number_of_threads)
    ]

    for t in threads:
        t.start()
 

    for t in threads:
        t.join()

    return max(shared_result) if shared_result else "failed"



# fibonacci part of project
def nth_fibo(n):
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b
    return b


# factorial part of project
def factorial_part(start, end, shared_result, lock):
    result = 1
    for i in range(start, end):
        result *= i

    with lock:
        shared_result[0] *= result

def factorial(n , number_of_threads):
    range_per_process = n // number_of_threads
    shared_result = [1.0]
    lock = threading.Lock()

    threads = [
        threading.Thread(
            target = factorial_part,
            args = (i * range_per_process + 1, (i + 1) * range_per_process + 1, shared_result, lock)
        )
        for i in range(number_of_threads)
    ] 

    for t in threads:
        t.start()
 

    for t in threads:
        t.join()
    
    return (shared_result[0])
    


if __name__ == "__main__":

    hp = highest_prime(time_limit= 0.5, number_of_threads= 10)
    print(hp)

    high_fibo = nth_fibo(hp)
    print(high_fibo)

    high_factorial = factorial(hp, 10)
    print(high_factorial)



