a = 25

if a > 30 and a < 100:
    print("A is greater than 30")

if not a > 30:
    print("a is not greater than 30")

if 20 <= a < 30:
    print("a is between 20 and 30")

#love calculator
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')
first_digit = t + r + u + e

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')
second_digit = l + o + v + e
score = int(str(first_digit) + str(second_digit))
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

