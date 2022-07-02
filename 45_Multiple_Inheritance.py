# Multiple Inheritance

class Father:
    @property
    def fishing(self):
        print("Fishing in Rivers")
    @property
    def chess(self):
        print("Playing Chess From Father")

class Mother:
    @property
    def cooking(self):
        print("Cooking Food")
    @property
    def chess(self):
        print("Playing Chess From Mother")    

class Son(Mother,Father):
    
    @property
    def ride(self):
        print("Riding Bicyle")

o=Son()
o.ride 
o.fishing
o.cooking
o.chess               
