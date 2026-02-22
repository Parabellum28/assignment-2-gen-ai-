birth_year = int(input("Enter your birth year: "))
current_year = 2026

age = current_year - birth_year

print("Current Age:", age, "years")
print("Age in months:", age * 12)
print("Age in days:", age * 365)
print("Age in hours:", age * 365 * 24)
print("Age in minutes:", age * 365 * 24 * 60)
print("Years until age 100:", 100 - age)

#but for precise age calculation, we need to import date and time from lib.