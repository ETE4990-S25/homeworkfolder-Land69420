import asyncio 
import time

# large prime part of project
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


async def primes_in_range(start, stepsize, result, time_limit):
    highest_prime = -1
    starttime = time.time()

    number = start

    while time.time() - starttime < time_limit:
        if is_prime(number):
            highest_prime = number
        number += stepsize

        await asyncio.sleep(0) # chat said this is necessary to hand priority to other processes IDK why tho

    result.append(highest_prime)


async def highest_prime(time_limit, number_of_tasks):
    print(f"finding largest prime in {time_limit} seconds.")

    shared_result = [-1]


    tasks = [
        asyncio.create_task(
            primes_in_range(2 * i + 1, number_of_tasks * 2, shared_result, time_limit)
        )
        for i in range(number_of_tasks)
    ]

    await asyncio.gather(*tasks)

    return max(shared_result) if shared_result else "failed"


# fibonacci part of project
def nth_fibo(n):
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b
    return b


# factorial part of project
async def factorial_part(start, end, shared_result, lock):
    """this is ur code from lecture"""
    result = 1

    for i in range(start, end):
        result *= i
        await asyncio.sleep(0) # I'm putting this in cause I'm assuming 
                                # inside of any loop it's better to let others interrupt as chatgpt described

    async with lock:
        shared_result[0] *= result



async def factorial(n, number_of_tasks):
    range_per_task = n // number_of_tasks
    shared_result = [1.0]  
    lock = asyncio.Lock()

    tasks = [
        asyncio.create_task(
            factorial_part(
                i * range_per_task + 1,
                (i + 1) * range_per_task + 1,
                shared_result,
                lock)
        )
        for i in range(number_of_tasks)
    ]

    await asyncio.gather(*tasks)

    return shared_result[0]


async def main():
    hp = await highest_prime(time_limit= 0.5, number_of_tasks= 10)
    print(hp)

    high_fibo = nth_fibo(hp)
    print(high_fibo)

    high_factorial = await factorial(hp, 10)
    print(high_factorial)





if __name__ == "__main__":
    asyncio.run(main())