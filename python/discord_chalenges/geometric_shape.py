"""Module providing a function printing python version."""

import math

shape = input('Enter the shape (1: Square, 2: Circle or 3: Triangle): ')

if shape.lower() == 'square' or shape == '1':
    side = float(input('Enter the length of one side: '))
    surface_area = pow(side, 2)
elif shape.lower() == 'circle' or shape == '2':
    radius = float(input('Enter the radius: '))
    surface_area = math.pi * pow(radius, 2)
elif shape.lower() == 'triangle' or shape == '3':
    side_1 = float(input('Enter the length of first side: '))
    side_2 = float(input('Enter the length of second side: '))
    side_3 = float(input('Enter the length of third side: '))

    # Checking if value of each side is valid
    if (side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_2 + side_3 > side_1):
        s = (side_1 + side_2 + side_3) / 2
        surface_area = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))
    else:
        print('Lengths are invalid. The sum of two sides must always exceed the third side.')
        surface_area = 'Invalid'
else:
    print('Invalid shape')
    surface_area = 'Invalid'

if isinstance(surface_area, (float)):
    print(f'The surface area is {surface_area:.4f}.')
