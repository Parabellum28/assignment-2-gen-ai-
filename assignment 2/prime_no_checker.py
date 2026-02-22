num=int(input("enter a number: "))
if num<=1:
    print(num,"is NOT a prime number")
elif num==2:
    print("2 is a PRIME number")
else:
    prime=True
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
    if prime:
        print(num,"is a PRIME number")
    else:
        print(num,"is NOT a prime number")