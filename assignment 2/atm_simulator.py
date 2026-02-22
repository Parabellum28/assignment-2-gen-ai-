balance = 69000
while True:
    print("\nATM SIMULATOR")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")

    choice =int(input("Enter choice:"))
    if choice==1:
        print("Current Balance: ₹",balance)
    elif choice==2:
        amount =int(input("Enter amount to deposit:"))
        balance =balance+amount
        print("Deposit successful!")
        print("New balance:₹",balance)
    elif choice==3:
        amount =int(input("Enter amount to withdraw:"))

        if balance-amount>=500:
            balance =balance-amount
            print("Withdrawal successful!")
            print("New balance:₹",balance)
        else:
            print("Insufficient balance! Minimum ₹500 must remain.")
    elif choice==4:
        print("Thank you for using ATM")
        break
    else:
        print("Invalid choice")