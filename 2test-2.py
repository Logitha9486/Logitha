try:
    n=int(input("Enter the Year:"))
    if(n>0):
        if(n%4==0 or n%400==0):
            print("It is a Leap Year!")
        else:
            print("It is not a Leap Year!")
    else:
        print("Not a valid Year!")
except:
    print("Not Valid Year")
