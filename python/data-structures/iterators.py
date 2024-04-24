nums = [10, 14, 21, 50, 5, -6]
spam = ['cat', 'dog']

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

squared_nums = list(map(square, nums))
even_numbers = list(filter(lambda x: x % 2 == 0, nums))
cubed_nums = list(map(lambda x: x ** 3, even_numbers))

# print(squared_nums)
# print(cubed_nums)
# print(even_numbers)

print(sorted(nums))
print(sorted(nums, reverse=True))

########################################################
# Sorting a dictionary

employees = [
    {'name': 'John', 'age': 36},
    {'name': 'Mary', 'age': 27},
    {'name': 'Bob', 'age': 40}
]

print(sorted(employees, key=lambda emp: emp['name']))

print(sorted(employees, key=lambda emp: emp['age']))

print(max(employees, key=lambda emp: emp['age']))

print(max(employees, key=lambda emp: emp['age'])['age'])

########################################################
# Alternative way
# To get the max of the ages
# First get the list of ages

print(list(map(lambda emp: emp['age'], employees)))

# Then get the max
print(max(map(lambda emp: emp['age'], employees)))