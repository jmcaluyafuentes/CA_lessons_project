# my_dog = {'name': 'Ted', 'age': 16, 'breed': 'Border Collie'} # this is hard coded

class Dog:
    # Constructor method
    def __init__(self, name):
        # Creates a new attribute 'name' on self and copies the value of 'name' parameter into it
        self.name = name
        self.action = 'sleeping'

    def greet(self, message='Hello'):
        print(f'{message} {self.name}')
