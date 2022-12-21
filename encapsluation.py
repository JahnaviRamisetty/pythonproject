class table:
    def __init__(self):
        self.__maxprice = 10000

    def sell(self):
        print("selling price {}".format(self.__maxprice))

    def set_max_price(self):
        self.__maxprice=15000

wood=table()
print(wood.sell())

wood.__maxprice = 15000
print(wood.sell())

wood.set_max_price()
print(wood.sell())