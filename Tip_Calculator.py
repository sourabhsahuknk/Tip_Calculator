#Tip Calculator:

print("Welcome to tip calculator! ")

total_bill = float(input("What was the total bill : "))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
split = float(input("How many people to split the bill? "))
tip_calculator = (total_bill + (total_bill*(tip/100))) / split
new_tip_calculator = round(tip_calculator,2)
new_tip_calculator = "{:.2f}".format(tip_calculator) #this is used because this is a formatting problem not a mathematical problem
print(f"Each person should pay {new_tip_calculator}")
