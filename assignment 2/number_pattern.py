print("choose Pattern")
print("pattern 1")
print("Pattern 2")
print("pattern 3")
print("pattern 4")

choice =int(input("Enter pattern number:"))
n =int(input("Enter height:"))
if choice==1:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()
elif choice==2:
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=" ")
        print()
elif choice==3:
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
elif choice==4:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        for j in range(i-1,0,-1):
            print(j,end="")
        print()
else:
    print("it is inavlid")