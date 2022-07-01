# try block in Python
try:
    a = 10/0
except Exception as e:
    print(e)
print("----------------------")

# Try Else
try:
    a = 10/25
except Exception as e:
    print(e)
else:
    print("A Value : ", a)

print("------------------------------")
# Try else finally

try:
    a = 10 / 0
except Exception as e:
    print(e)
else:
    print("A Value : ", a)
finally:
    print("Thank You")
print("-------------------------------")

# Type of Exceptions in Python
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

print("-----------------------------------")

# Nameerror Exception
try:
    print(c)
except NameError as e:
    print("c is not Defined")

try:
    print(10/0)
except ZeroDivisionError as e:
    print("denominator cant be zero")

try:
    a = int("Joes")
except ValueError as e:
    print("Please Enter Numbers Only")

try:
    a = [10, 20, 30, 40]
    print(a[10])
except IndexError as e:
    print("Invalid Index")

try:
    f = open("23_Tupe.py")
except FileNotFoundError:
    print("File Not Found")
else:
    print(f.read())

print("----------------------------------")

try:
    a=10/20
    print(a)
    b=[10,20,30,40]
    print(b[0])
    a=open('ramu.txt')
except ZeroDivisionError:
    print("denominator cant be zero")
except IndexError:
    print("Invalid Index")
except Exception as e:
    print(e)

