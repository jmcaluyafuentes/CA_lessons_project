spam = ['cat', 'dog', 'bird', 'cat']
eggs = [12, 78, 100, 5.4, 42]
person = ['John', 36]

# print(spam)
# print(type(spam))
# print(len(spam))
# print(eggs)
# print(person)
# print(eggs[1])

tic_tac_toe = [
    ['', '', ''],
    ['', 'X', ''],
    ['', '', '']
]

# print(tic_tac_toe[1][1])

# print(person + spam)

# person.extend(spam)
# person.insert(1, 185)
# person.clear('cat')
# print(person)

# for i in range(len(spam)):
#     print(spam[i])

# for animal in spam:
#     print(animal)

# print(list(range(1, 10, 2)))

# index = 1
# for animal in spam:
#     print(f'{index}. {animal}')
#     index += 1

# print(list(enumerate(spam)))

# for index, animal in enumerate(spam, 1):
    # print(f'{index}. {animal}')

# print(spam.index('bird'))

# print('bird' in spam)

# x = 'bird'
# if x in spam:
#     print(spam.index(x))


# x = 'dsaf'
# print(spam.index(x) if x in spam else 'Not Found')

############################
# def display_person(person):
#     print(f'{person[0]} is {person[1]} years old and {person[2]} cm tall.')

# me = ['John', 36, 178]
# display_person(me)

############################
# def display_person(person):
#     name = person[0] # first name
#     age = person[1]
#     height = person[2]
#     print(f'{name} is {age} years old and {height} cm tall.')

# me = ['John', 36, 178]
# display_person(me)

############################
def display_person(person_info):
    name, age, height = person_info # This is called 'unpacking'
    [name, age, height] # can make the variables into a list
    print(f'{name} is {age} years old and {height} cm tall.')

me = ['John', 36, 178]
display_person(me)

