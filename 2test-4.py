lst1=[]
lst2=[]
flag=0
n=int(input("Enter the size of the list:"))
if(n>0):
    flag=1
    print("Enter a number:")
    for i in range(0,n):
        ele=int(input())
        lst1.append(ele)
    flag=1
elif(n==0):
    lst1=[]
    flag=0
else:
    flag=3
m=int(input("Enter the size of the list2:"))
if(m>0):
    print("Enter a number:")
    for i in range(0,m):
        el=int(input())
        lst2.append(el)
    flag=1
elif(m==0):
    lst2=[]
    flag=0
else:
    flag=3
if(flag==1):
    lst=lst1+lst2
    lst.sort()
    print(lst)
else:
    lst=lst1+lst2
    print(lst)
