x=int(input("Input : "))
n=1
y=x-1
for i in range(x):
    for j in range(x-n):
        print(" ",end="")
    for j in range(x-y):
        print("*",end=" ")
    print("\r")
    n=n+1
    y=y-1
n=x-1
y=1
for i in range(x-1):
    for j in range(x-n):
        print(" ",end="")
    for j in range(x-y):
        print("*",end=" ")
    print("\r")
    y=y+1
    n=n-1
