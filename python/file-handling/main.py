# with open('shopping-list.txt') as f: # 'with' is a context manager
#     data = f.read(5) # the program keep tracts on how many files being read with internal counter
#     foo = f.readline()
#     spam = f.read(5)
#     print(data)
#     print(foo)
#     print(spam)
    
    # when f (the file) gets out of scope of the with block, the file will close automatically

# with open('tv-shows', 'w') as f:

# import csv

# # with open('people.csv') as f:
# #     reader = csv.DictReader(f)
# #     # reader = csv.reader(f)
# #     # reader.__next__()
# #     for row in reader:
# #         # print(f'{row[0]} is {row[1]} years old.')
# #         print(f"{row['name']} is {row['age']} years old.")

menu = [
    {'foo': 'Cappucino', 'price': 6.50},
    {'foo': 'English Breakfast Tea', 'price': 5},
    {'foo': 'Blueberry Muffin', 'price': 6}
]

# with open('cafe-menu.csv', 'w') as f:
#     # writer = csv.DictWriter(f, ['item', 'price'])
#     writer = csv.DictWriter(f, menu[0].keys())
#     writer.writeheader()
#     writer.writerows(menu)

import json

with open('movies.json') as f:
    movies = json.load(f) # load method converts json to python objects
    m = movies[2]
    print(f"{m['title']}")

with open('menu.json', 'w') as f:
    json.dump(menu, f, indent=4) # dump menu converts python data structure to json

result = json.dumps(menu, indent=4)
print(result)
