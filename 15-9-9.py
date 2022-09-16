def shuffle(l1,l2):
    for i in range(p):
        if(i<a):
            f.append(c[i])
        if(i<d):
            f.append(e[i])
            print(f)
a=int(input("Enter the number of elements l1:"))
c=[]
e=[]
f=[]
for i in range (a):
    b=int(input("ENTER:"))
    c.append(b)
d=int(input("Enter the number of elements l2:"))
for i in range (d):
    z=int(input("ENTER:"))
    e.append(z)
p=a+d
shuffle(c,f)
