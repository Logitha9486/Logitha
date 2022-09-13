from itertools import permutations
s=int(input("Enter length of list:"))
b=[]
c=[]
for i in range(0,s):
    a=int(input("Enter element:"))
    b.append(a)
perm=permutations(b)
for i in list(perm):
    if i not in c:
        c.append(i)
print("OUTPUT=",c)
