print(3+5)
print(3-5)
print(3*2)
print (6/3) #dividing always converts the type into a float even if it goes directly
print(2**3) #this is an exponent 2^3 = 8

#order of priority: Parentheses -> exponents -> multiplication / division -> addition / subtraction

#bmi calculator

height = input("Enter your height\n")
weight = input("Enter your weight\n")

height = float(height)**2
weight = float(weight)
bmi = weight/height
bmi = int(bmi)

print(bmi)

#number manipluation
round_numer = round(25.6) #rounds into a whole number
two_decimals = round(23.45234,2) #rounds to two decimal places

no_decimals = (8//3) #this removes any deciamls after divistion

#f-string
score = 23
height = 12.23
winning = True
sen = f'your score is{score}, your height is {height}, you are winning {winning}'

#weeks left till 90 years old
age = input("Enter your age\n")

age = int(age) #convert to int data type
years_left = 90 - age #years left till 90
weeks_left = years_left * 52
weeks_left = str(weeks_left)

print("You have " + weeks_left + " weeks left.")