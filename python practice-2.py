1. Fibonacci series
def fab(n):
  a,b=0,1
  series=[]
  for _ in range(n):
    series.append(a)
    a,b = b,a+b
  return(series)
print(fab(10))
==========================================
2. to find the number is prime or not:

def prime(n):
  if n<=1:
    return False
  if n==2:
    return True
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
     return False
  return True

num=10
print(prime(num))
=========================================
3. to print prime numbers from 1 to 100:

def prime(n):
  if n<=1:
    return False
  if n==2:
    return True
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
     return False
  return True

for num in range(1,101):
  if prime(num):
    print(num,end=" ")
===========================================
4. To take only alphabets from a string:

def digit(n):
  result =""
  for i in n:
    if i.isalpha():
      result +=i
  return result    

txt ="iqwan123" 
print(digit(txt))
   ** output:iqwan
=============================
5. To take only numeric value from a string:

def digit(n):
  result =""
  for i in n:
    if i.isdigit():
      result +=i
  return result    

txt ="iqwan123" 
print(digit(txt))
   ** output:123
==============================
6. write first non-repeated word in the string. 

def non(s):
  char={}

  for i in s:
    char[i]=char.get(i,0)+1
  for i in s:
    if char[i]==1:
      return i
  return none

text="bbaaccd"
print(non(text))

**output: d

============(or)=====
for i in s:
    if s.count(i) == 1:
        print(i)
        break
