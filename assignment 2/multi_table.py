num =int(input("Enter number:"))
end =int(input("enter range(when u want to end):"))
print("Multiplication Table of",num)
for i in range(1,end+1):
    print(num,"x",i,"=",num*i)