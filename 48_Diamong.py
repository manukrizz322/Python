class A:
    def display(self):
        print("I am the display of Class A")

class B(A):
    def display(self):
        print("I am the display of Class B")        

class c(A):
    def display(self):
        print("I am the display of C")

class D(B,c):
    def display(self):
        print("I am the display of class D")        

o=D()
o.display()      