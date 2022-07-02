# Multilevel Inheritance
class Grandfather:
    @property
    def ownHouse(self):
        print("Grandpa House")

class Father(Grandfather):
    @property
    def ownBike(self):
        print("Father's Bike")        

class Son(Father):
    @property
    def ownBook(self):
        print("Son Have a Book") 

o=Son()
o.ownHouse
o.ownBike
o.ownBook
