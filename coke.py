
amount_due = 50

while amount_due >= 0:
    print(f"Amount Due: {amount_due}")
    x = int(input("Insert coin: "))

    if x in [5, 10, 25]:
        amount_due -= x
        print("Amount Due 50")
    
    if amount_due == 0:
        print("Change owed:", abs(amount_due))
        break
