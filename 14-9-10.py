a=input("Enter s1:")
b=input("Enter s2:")
if(len(a)==len(b)):
    if(len(a)!=1):
        e=a[:int(len(a)/2)]
        e1=a[int(len(a)/2):]
        f=b[:int(len(b)/2)]
        f1=b[int(len(b)/2):]
        g=''.join(sorted(e))
        g1=''.join(sorted(e1))
        h=''.join(sorted(f))
        h1=''.join(sorted(f1))
        if(g==h):
            if(g1==h1):
                print("True")
            else:
                print("False")
        else:
            print("False")
    else:
        print("True")
else:
    print("False")
