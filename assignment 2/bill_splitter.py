bill =float(input("Enter total bill:"))
people =int(input("Number of people:"))
tax_percent =float(input("Tax percentage:"))
tip_percent =float(input("Tip percentage:"))

tax =bill*tax_percent/100
after_tax =bill+tax

tip =after_tax*tip_percent/100
total =after_tax+tip

per_person = total / people

print("=== BILL BREAKDOWN ===")
print("Subtotal:₹{:.2f}".format(bill))
print("Tax ({}%):₹{:.2f}".format(tax_percent,tax))
print("After tax:₹{:.2f}".format(after_tax))
print("Tip ({}%):₹{:.2f}".format(tip_percent,tip))
print("Total:₹{:.2f}".format(total))
print("Per person:₹{:.2f}".format(per_person))