nums = [10, 14, 21, 50, 5, -6]

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

squared_num = list(map(square, nums))
cubed_num = list(map(cube, nums))

print(squared_num)
print(cubed_num)
