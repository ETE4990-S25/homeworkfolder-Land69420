import math
import functools

#even odd lambda function
evenodd = lambda x: "odd" if x%2 else "even"

print(evenodd(2))
print(evenodd(3))


#lambda function that sums a list
list_to_sum = lambda alist: sum(alist)

print(list_to_sum([1,2,3,4]))

#lambda function that sorts a list
sorted_list = lambda alist: sorted(alist)

print(sorted_list([45,34,32,12]))


#lambda function that calls filter and filter calls a function that returns true or false to filter a list
#I stole the is_prime() off the internet. just needed something that gives true or false.
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

filtered_list = lambda alist: list(filter(is_prime,alist))

print(filtered_list([1,5,6,7,8,11,31]))



#lambda function that uses map, it being a lambda is completely unecessay and just the map would do but I put it in a lambda
def times2(number):
    return number * 2

list_times_2 = lambda alist: list(map(times2,alist))
print(list_times_2([1,2,3,4,5]))


#using lambda function and reduce to find the sum of a list
list_to_sum_with_reduce = lambda alist: functools.reduce(lambda x, y: x + y, alist)

print(list_to_sum_with_reduce([1,2,4,56,6]))

#lambda function using enumerate
# associates each item with a number
numbered_items_in_list = lambda alist:list(enumerate(alist, start = 1))

print(numbered_items_in_list(["this","is","a","list","of","words","to","be","numbered"]))

#zip with lambda function
zip_two_lists = lambda alist, blist: list(zip(alist,blist))

sentence = ['list', 'of', 'words', 'to', 'be', 'associated', 'with', 'another', 'list', 'of', 'words']
randwords = ['sunflower', 'tiger', 'ocean', 'mountain', 'keyboard', 'puzzle', 'guitar', 'starlight', 'whisper', 'universe', 'adventure']
print(zip_two_lists(sentence,randwords))

