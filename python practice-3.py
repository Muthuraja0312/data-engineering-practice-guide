1.To print middle element in the list:

a=[12,31,34,99,21]
b=int(len(a)/2)
print(a[b])

**output:34

2.finds the missing numbers in a sequence
Lis =[1,2,4]
missing = []

for i in range(min(Lis), max(Lis) + 1):
    if i not in Lis:
        missing.append(i)

print(missing)

3.what will be the output ?
d1 = {"a": 1, "b": 2}
d2 = {"b": 5, "c": 7}

d3 = {**d1, **d2}

print(d3)
***output:{'a': 1, 'b': 5, 'c': 7}
==================================
4..what will be the output ?
A = [1, 2, 3]
B = A
C = [1, 2, 3]

print(A == C)
print(A is C)
print(A is B)
***output: 
True
False
True
=========================================
5.what will be the output ?
x = 100

lst = [x for x in range(3)]

print(lst)
print(x)
*** output:
[0, 1, 2]
100
==========================================
