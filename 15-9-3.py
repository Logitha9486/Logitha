n=int(input("Enter the number:"))
c=0
e=0
while(n>0):
    d=n%10
    c=c+d
    n=n//10
for i in range(1,c+1):
    if(i*i<=c):
        e+=1
print("Number of least perfect square numbers:",e)
