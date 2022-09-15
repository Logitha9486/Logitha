a=int(input("Total user:"))
if(a<0):
    print("INVALID INPUT")
elif(a==0):
    print("There is no staff and student user")
else:
    b=int(input("Staff user:"))
    if(b<0):
        print("INVALID INPUT")
    elif(b==0):
        print("Student user =",a)
    elif(a<b):
        print("INVALID INPUT")
    elif(a==b):
        print("Student user =0")
    else:
        c=a-b
        d=c-b/3
        print("Student user =",int(d))
