1. To create a function to add two values:

def addfun(x,y):
  return(x+y)

print(addfun(15,5))

2.to get input from user:

x=int(input ("enter value x :"))
y=int(input ("enter value y :"))

def addfun(x,y):
  return(x+y)

print(addfun(x,y))

3.python function -> accept 2 arguments(int), multiply and check odd or even 

x=int(input ("enter value x :"))
y=int(input ("enter value y :"))

def addfun(x,y):
     z=x*y
     if z%2==0:
       return(z,"even")
     else:
       return("odd",z)
print(addfun(x,y))

4.pass,continue,break

for i in range(5):
    if i == 2:
        pass
    print(i)

for i in range(5):
    if i == 2:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

5.what is decorator and example code:
A decorator is a function that allows you to add/modify behavior of another function without changing its original code.
def my_decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@my_decorator
def hello():
    print("Hello!")


hello()
===============================================================
6.what is the difference b/w parameter and arguments:

Parameter = variable defined in the function.
Argument = actual value passed to the function.
def add(x, y):
    return x + y

add(10, 20)
x and y  → Parameters
10 and 20 → Arguments

Types of arguments
Python supports different ways of passing arguments.

1. Positional arguments
def add(x, y):
    return x + y

add(10, 20)

10 goes to x, and 20 goes to y.

2. Keyword arguments
add(x=10, y=20)

Here you're explicitly specifying which parameter gets which value.

3. Default parameters
def greet(name, message="Hello"):
    print(message, name)

greet("Iqwan")

message has a default value of "Hello".
===================================================================
7. try/except:
  I use try-except blocks to handle runtime exceptions. I generally catch specific exception types such as ValueError, FileNotFoundError, or ZeroDivisionError instead of using a generic except. I can use else for code that should execute when no exception occurs, and finally for cleanup operations that must execute regardless of whether an exception occurred.

try      → Code that might fail
except   → Handle the error
else     → Runs if no error
finally  → Always runs
raise    → Manually generate an exception
======================================================================
8. to reverse the string using a function

def rev(a):
  return(a[::-1])

print(rev("iqwan"))
===================================================
9.reverse the list and inside rever the string also:

a=["iqwan","deepika","kaushi"]

rev1 =[i[::-1] for i in a]
def rev(a):
  return(a[::-1])
print(rev(rev1))
=============================================
10. to reverse the string using for loop:
a="iqwan is learning"
for i in a.split():
  print(i[::-1],end =' ')
