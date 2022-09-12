E=[]
L=[]
t = int(input("T="))
try:
    if(t>0):
        for i in range(t):
            e=int(input("Guest entered="))
            E.append(e)
        for i in range(t):
            l=int(input("Guest Leaved="))
            L.append(l)
        S=0
        M=0
        for i in range(t):
            S+=E[i]-L[i]
            M=max(S,M)
        print("E=",E)
        print("L=",L)
        print("output=",M)
    else:
        print("INVALID T VALUE")
except ValueError:
    print("Enter all values ")
