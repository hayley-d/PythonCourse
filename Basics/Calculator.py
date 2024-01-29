print("Welcome to the tip calculator")
bill = int(input("Enter the bill totoal\n"))
tip_percent = 0.1

bill_with_tip = bill + (bill * tip_percent)

print(f"Your bill with the tip comes to {bill_with_tip:.2f}")