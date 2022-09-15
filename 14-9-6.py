a=input("Enter a string:")
b=input("Enter character to be deleted :")
c=len(a)
d=""
for i in range(0,c):
    if a[i] not in b:
        d+=a[i]
print("String after deletion :",d)
