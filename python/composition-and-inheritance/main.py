from rpg import Character, Chest, Fridge

aragorn = Character(race='Human', name='Aragorn')
galadriel = Character('Galadriel', 'Elf')
frodo = Character('Frodo', 'Hobbit', gold=50)

chest1 = Chest(items=['longsword', 'arrow'], gold=25, locked=True)

fridge1 = Fridge(locked = True)

print(aragorn.inv.__dict__)
print(aragorn.chiller.__dict__)
print(chest1.inv.__dict__)
print(fridge1.chiller.__dict__)

chest1.inv.transfer(aragorn.inv)
fridge1.chiller.transfer(aragorn.chiller)

print(aragorn.inv.__dict__)
print(aragorn.chiller.__dict__)
print(chest1.inv.__dict__)
print(fridge1.chiller.__dict__)

