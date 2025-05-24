name = input("Hello what is your name? \n").upper()

apple = input("Welcome " +name+ " do you want to buy apple at 20.0 rate: \n")
if apple.lower() == 'yes':
    aQty = int(input("How many? \n"))
else: (aQty) = 0

mango = input("Do you want to buy mango at 15.0 rate: \n")
if mango.lower() =='yes':
    mQty = int(input("How many? \n"))
else: (mQty) = 0

orange = input("Do you want to buy orange at 10.0 rate: \n")
if orange.lower() =='yes':
    oQty = int(input("How many? \n"))
else: (oQty) = 0

print("This is the list you bought from our store:")
print(str(aQty), "pcs of apples ----------", aQty*20.0)
print(str(mQty), "pcs of mangoes ----------", aQty*15.0)
print(str(oQty), "pcs of oranges ----------", aQty*10.0)
print("==========")

to=(aQty * 2.0 + mQty * 15.0 + oQty * 10.0)
print("Total: ", to, "\n")

print("Hello", name, "!")
if to >= 200:
    print("Total payment ----------", to)
    discount = to - (to * 0.20)
    print("Discount ----------", discount)
    cash = int(input("Cash Tendered ----------"))
    print("Change ----------", (cash - discount))
else:
    print("Total payment ----------", to)
    cash = int(input("Cash Tendered ----------"))
    print("Change ----------", (cash-to), "\n")
    
print("Thank you for buying!")