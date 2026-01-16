import random
class Amarine:
    __unit_total = 0
    __price_total = 0
    def __init__(self,id, name, type):
        self.__id = id
        self.__name = name
        self.__type = type
    #getter
    def getName(self):
        return self.__name
    def getType(self):
        return self.__type
    
    #setter
    def setName(self, name):
        self.__name = name

    def setType(self, type):
        self.__type = type

    def addPrice(self, price):
        self.__price_total += price
    def totalPrice(self):
        print(f"Total Harga Kapal: Rp. {self.__price_total:,}")
    def totalUnit(self):
        Amarine.__unit_total += 1
        print(f"Total Kapal: {Amarine.__unit_total}")
    def info(self):
        print(f"Nama Kapal: {self.getName()}")
        print(f"Tipe Kapal: {self.getType()}")
        self.totalPrice()
        print(f"Harga Kapal: Rp. {self.__price_total:,}")
        self.totalUnit()
        print("=================================")

nilai_random = random.randint(1,100)

amarine1 = Amarine(nilai_random, "AMN-01", "Fishing Boat")
amarine2 = Amarine(nilai_random, "AMN-02", "Armed Boat")
amarine3 = Amarine(nilai_random, "AMN-03", "Attack Boat")
amarine4 = Amarine(nilai_random, "AMN-04","Defense Boat")
container = [amarine1, amarine2, amarine3, amarine4]

for i in container:
    i.addPrice(random.randint(10000000, 99999999))

for i in container:
    i.info()
    