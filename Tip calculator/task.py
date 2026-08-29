print("Welcome to the tip calculator!" )
bill=float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
splitBill = int(input ("How many people to split the bill?"))
totalTip = bill*(tip/100)
totalBill= bill+totalTip
eachPerson = (totalBill/splitBill)
print(f"Each person should pay: ${eachPerson:.2f}")