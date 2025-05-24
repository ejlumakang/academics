def coke_machine():
    total_paid = 0
    while total_paid < 50:
        coin = input("Please insert a coin (5, 10, or 25 cents): ")
        if coin == "5":
            total_paid += 5
        else:
            if coin == "10":
                total_paid += 10
            else:
                if coin == "25":
                    total_paid += 25
                else:
                    print("Invalid coin. This machine only accepts 25, 10, or 5 cent coins.")
        amount_due = 50 - total_paid
        if amount_due > 0:
            print(f"Amount due: {amount_due} cents")
    change = total_paid - 50
    if change > 0:
        print(f"You are owed {change} cents in change.")
    else:
        print("Thank you for your purchase.")

coke_machine()