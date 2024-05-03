class Inventory:
    def __init__(self, gold=0, items=[]):
        self.gold = gold
        self.items = items

    def transfer(self, to_inv):
        to_inv.gold += self.gold
        self.gold = 0
        to_inv.items += self.items
        self.items = []

class Character:
    def __init__(self, name, race, gold=0, items=[], food = []):
        self.name = name
        self.race = race
        self.inv = Inventory(gold, items)
        self.chiller = Chiller(food)
        
class Chest:
    def __init__(self, items=[], gold=0, locked=False):
        self.locked = locked
        self.inv = Inventory(gold, items)