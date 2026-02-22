age = int(input("Enter age:"))
day = input("Enter day of week:")
tickets = int(input("Number of tickets:"))
if age <3:
    price =0
    category ="Free"
elif age <=12:
    price =150
    category ="child"
elif age <=59:
    price =300
    category ="adult"
else:
    price =200
    category ="senior"

base_amount =price *tickets

if day in ["friday","saturday","sunday"]:
    discount =base_amount *0.20
else:
    discount =0

final_amount =base_amount -discount
print("BILL DETAILS")
print("Category:",category)
print("Base price per ticket: ₹",price)
print("Base amount: ₹",base_amount)
print("Discount: ₹",discount)
print("Amount after discount: ₹",final_amount)