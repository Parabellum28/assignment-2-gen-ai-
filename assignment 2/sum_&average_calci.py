n =int(input("how many numbers?:"))
total=0
max_num=None
min_num=None
for i in range(1,n+1):
    num =int(input("enter number"+str(i)+":"))
    total=total+num
    if max_num is None or num>max_num:
        max_num=num
    if min_num is None or num<min_num:
        min_num=num

average =total/n
print("Sum:",total)
print("Average:",average)
print("maximum:",max_num)
print("minimum:",min_num)