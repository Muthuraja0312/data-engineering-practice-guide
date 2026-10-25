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
