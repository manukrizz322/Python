# Getting String input Statement
"""name = input("Enter Name : ")
print(type(name))
print(name)

# Getting Integer input Statement
a = int(input("Enter the value of A : "))
b = int(input("Enter the Value of B: "))
c = a+b
print(c)
print(type(a))

# Getting Float input Statement
a = float(input("Enter the value of A : "))
b = float(input("Enter the value of B : "))
c = a+b
print(c)
print(type(a))"""

# Multiple Values in Single line
"""name1, name2, name3 = input("Enter 3 Names: ").split()
print("Name 1 : ", name1)
print("Name 2 : ",name2)
print("Name3 : ",name3)

name1,name2,name3=input("Enter 3 Names : ").split(',')
print("Name 1 : ",name1)
print("Name 2 : ",name2)
print("Name 3 : ",name3)"""

# Multiple Line String Input in Python
a = """
Lorem Ipsum is simply dummy text
of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard
dummy text ever since the 1500s,
"""
print(type(a))
print(a)

para = []
print("Enter a Para : ")

while True:
    line = input()
    if line:
        para.append(line)
    else:
        break
    print(para)
    output = '\n'.join(para)
    print(output)
