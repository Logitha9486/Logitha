b=int(input("enter lenght of array"))
a=[]
e=[]
for i in range(0,b):
    c=input("enter a string")
    a.append(c)
for i in range(0,b):
    d=len(a[i].split())
    e.append(d)
print("list =",a)
print("max word in a string =",max(e))
