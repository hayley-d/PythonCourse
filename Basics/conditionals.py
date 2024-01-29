print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

#conditional
if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry you are not tall enough :(")

#nested if statements
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 18:
        print("Ticket is $8")
    else:
        print("Ticket is $10")
else:
    print("Sorry you are not tall enough :(")

#elif statements

height = float(input())
weight = int(input())

bmi = weight/(height**2)
if bmi < 18.5:
  print(f'Your BMI is {bmi}, you are underweight.')
elif 18.5 <= bmi < 25:
  print(f'Your BMI is {bmi}, you have a normal weight.')
elif 25 <= bmi < 30:
  print(f'Your BMI is {bmi}, you are slightly overweight.')
elif 30 <= bmi < 35:
  print(f'Your BMI is {bmi}, you are obese.')
else:
  print(f'Your BMI is {bmi}, you are clinically obese.')

  #pizza delivery system
  print("Thank you for choosing Python Pizza Deliveries!")
  size = input()  # What size pizza do you want? S, M, or L
  add_pepperoni = input()  # Do you want pepperoni? Y or N
  extra_cheese = input()  # Do you want extra cheese? Y or N

  order_total = 0
  if size == 'S':
      order_total += 15
      if add_pepperoni == 'Y':
          order_total += 2
  elif size == 'M':
      order_total += 20
      if add_pepperoni == 'Y':
          order_total += 3
  else:
      order_total += 25
      if add_pepperoni == 'Y':
          order_total += 3

  if extra_cheese == 'Y':
      order_total += 1

  print(f"Your final bill is: ${order_total}.")
