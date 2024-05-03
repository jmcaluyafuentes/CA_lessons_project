class House:
    def __init__(self, price):
        self.__price = price

    # def display_price(self):
    #     print(f'Price is {self.__price}')

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print('Price must be greater than zero')

my_house = House(800000)
# my_house.price = 20000
# my_house.display_price()
# my_house.set_price(900000)
my_house.price = -900000
# print(my_house.price())
print(my_house.price)