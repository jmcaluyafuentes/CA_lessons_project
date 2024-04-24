import random

x = random.randint(10, 20)
print(x)

####################################
from random import randint, choice

x = randint(10, 20)
print(x)

animals = ['cat', 'dog', 'horse']
print(choice(animals))

####################################
# Using list comprehension
from random import randint, choice

random_num = [random.randint(10, 20) for i in range(10)]
print(random_num)

####################################
greeting = 'Hello World'
nums = [10, 20, 30]
person = {'name': 'John', 'age': 21}

def foo(person):
    print(f'{person.get("name", "Someone")} is {person.get("age", "unknown")} years old.')

foo(person)

####################################
import my_module

print(my_module.person)
print(my_module.greeting)

####################################
import my_module

my_module.foo(my_module.person)

# print(my_module)
# print(dir())
print(dir(my_module))

####################################
from my_module import foo, person

# my_module.foo(my_module.person)
foo(person)

####################################
from my_module import foo, person, greet

foo(person)
greet()