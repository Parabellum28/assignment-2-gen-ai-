print(" GRADE CALCI")
crypto =int(float(input("cryptography:")))
cloud =int(float(input("cloud computing:")))
cn =int(float(input("computer network:")))
dsa =int(float(input("DSA:")))
aws =int(float(input("AWS:")))

total =crypto+cloud+cn+dsa+aws
percent =total/5

print("Total:",total)
print("Percentage:",percent)

if crypto>=40 and cloud>=40 and cn>=40 and dsa>=40 and aws>=40:
    result ="Pass"
else:
    result ="Fail"
if percent>=90:
    grade ="A+"
elif percent>=80:
    grade ="A"
elif percent>=70:
    grade ="B"
elif percent>=60:
    grade ="C"
elif percent>=50:
    grade ="D"
else:
    grade ="F"
print("Grade:",grade)
print("Result:",result)