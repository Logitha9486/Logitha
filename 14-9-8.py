def roman(n):
    v={"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    value = 0
    l= 0  
    for i in n[::-1]:              
        d=v[i]
        if d>=l:        
            value+= d         
            l=d
        else:                                      
            value -= d

    return value
a=input("Enter Roman numeral")
print(roman(a))
