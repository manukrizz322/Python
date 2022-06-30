"""def welcome():
    print("Welcome To Tutor Joes")
welcome()   """

# No Return Type Without Argument Function in Python
"""def add():
    a=int(input("ENter the Value of A : "))
    b=int(input("Enter the VAlue of B : "))
    c=a+b
    print("Total",c)
add()    """

# No Return Type With Argument Function in Python
"""def sub(a,b):
    c=a-b
    print("Difference : ",c)
sub(23,3)  """

# Return Type Without Argument Function in Python
"""
def mul():
    a=int(input("Enter the Value of A : "))
    b=int(input("Enter the Value of B : "))
    c=a*b
    return c
x=mul()   
print("Mul",x) """

# Return Type With Argument Function in Python
"""
def div(a,b):
    c=a/b
    return c
x=div(25,2)    
print("Division ", x)"""

# Arbitrary Arguments Function in Python (*)

"""def class_10(*students):
    print(students)
    for user in students:
        print(user)
class_10("Ram","Sam","Raja","Sara")"""

# Keyword Arguments Function in Python
"""
def message(name,age):
    print(name, "age is ",age)
message(age=25,name="Ram")"""

# Arbitrary Keyword Arguments in Python(**)
"""
def user(name,city="Salem"):
    print(name,"is from",city)
user("Ram","Namakal")    
user("Sam")
"""
# Passing a List as an Argument in Function Python
"""
def total(marks):
    return sum(marks)
 
 
print("Total : ",total([55, 75, 80, 95, 47]))
"""
# recursive function
# 1 * 2 * 3 * 4 * 5=120
""""
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))    
print("Factorial : ",factorial(5))"""


def c(a): return a+50


print(c(5))


def c(a, b): return a*b


print(c(10, 25))
