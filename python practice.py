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
