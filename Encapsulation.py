class computer:
    def __init__ (self): 
        self.__maxprice = 900
    def sell(self):
        print(f"Selling Price: {self.__maxprice}")
    def setMaxPrice(self, price):
        self.__maxprice = price
c1 = computer()
c1.sell()
c1.__maxprice = 1000
c1.sell()
c1.setMaxPrice(1000)
c1.sell()

    