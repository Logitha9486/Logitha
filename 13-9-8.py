try:
    b=int(input("Enter no of srings in a list:"))
    a=[]
    f=[]
    for i in range(0,b):
        c=input("Enter Strings:")
        if(int(c)==12345):
            print("INVALID STRING")
        else:
            a.append(c)
            print(c)
    g={}
    for w in a:
        d=''.join(sorted(w))
        if d not in g:
            g[d]=[w]
        else:
            g[d]+=[w]
    for i in g:
        f.append(g[i])
    print(f)
except ValueError:
    print("Invalid string")
