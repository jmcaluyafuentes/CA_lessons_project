"""
Example 1
"""
def my_decorator(func: 'function'):
    def wrapper():
        print('before func')
        func()
        print('after func')
    return wrapper

@my_decorator
def my_function():
    print('This is my function')

# x = my_decorator(my_function)

# x()

my_function()

###########################################
"""
Example 2
"""

def greeting(func):
    def wrapper():
        value = input('What is your name: ')
        func(value)
    
    return wrapper

@greeting
def greet(name):
    print(f'Hi, {name}!')

# def get_name():
#     return input('What is your name: ')

# greeting(get_name())

# y = greeting(get_name)

# y()

greet()