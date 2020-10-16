import time
import random
from libery import MicroLibrary

# 1
'''There is string s = "string".
Write the code that reverses string,
i.e. returns "gnirts"'''
print("string"[::-1])

# 2
'''What is the purpose of decorators?'''

print(
    '''Decorator is a function that takes another function (decorated function)
    as an input and it can execute extra logic
    before/after trigering decorated function'''
)

# 3
'''Write decorator that measures function execution
time and print it to output console.'''


def timer(func):
    def wrapper():
        start = time.time()
        func()
        elapsed = time.time() - start
        return elapsed

    return wrapper

@timer
def sleep_function():
    time.sleep(3)

print(sleep_function())

# 4
'''Create micro library that allows users
to work with notes about books authors.
Note should contain author_name, note,
rating (rating - is 0 - 1 rating of the author)
Micro lib should contain the next funcitonality'''

num = random.random()
num = '%.2f' % num
name_list = ['Andrii', 'German', 'Taras', 'Ihor', 'Oles', 'Ira']

index = random.randint(0, 5)
index_name = name_list[index]
aut1 = MicroLibrary(f'{index_name}', f'{num}')

aut1.add_note()
aut1.read_from_file()
aut1.dell_from_file()
aut1.highest_rating()
aut1.lower_rating()
aut1.average_rating()
