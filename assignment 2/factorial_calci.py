n=int(input("enter a number: "))
if n<0:
    print("Factorial is not defined for negative numbers.")
elif n==0:
    print("0!=1")
else:
    fact=1
    print(str(n)+"!=",end=" ")
    for i in range(n,0,-1):
        fact=fact*i
        print(i,end="")
        if i !=1:
            print("×",end="")
    print("=", fact)