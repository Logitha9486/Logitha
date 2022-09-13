def minJumps(arr, l, h):
    if (h == l):
        return 0
    if (arr[l] == 0):
        return float('inf')
    min = float('inf')
    for i in range(l + 1, h + 1):
        if (i < l + arr[l] + 1):
            jumps = minJumps(arr, i, h)
            if (jumps != float('inf') and
                       jumps + 1 < min):
                min = jumps + 1 
    return min
n=int(input("Enter length of list:"))
arr=[]
for i in range(0,n):
    b=int(input("Enter element:"))
    arr.append(b)
print("arr[]=",arr)
print("Minimum jumps:",minJumps(arr, 0, n-1))
