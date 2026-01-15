import random
class Amarine:
    __unit_total = 0
    __price_total = 0
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

    def addPrice(self, price):
        self.__price_total += price
    def totalPrice(self):
        print(f"Total Harga Kapal: Rp. {self.__price_total:,}")
    def totalUnit(self):
        Amarine.__unit_total += 1
        print(f"Total Kapal: {Amarine.__unit_total}")
    def info(self):
        print(f"Nama Kapal: {self.name}")
        print(f"Tipe Kapal: {self.type}")
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

