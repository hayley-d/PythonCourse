import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = int(input('What do you choose?\nType 0 for Rock\nType 1 for Paper\nType 2 for Scissors\n'))
if choice == 0:
    print("Rock")
    print(rock)
    choice = 0
elif choice == 1:
    print("Paper")
    print(paper)
elif choice == 2:
    print("scissors")
    print(scissors)

computer_choice = random.randint(0,2)
print(f"Computer chose\n")

if computer_choice == 0:
    print("Rock")
    print(rock)
elif computer_choice == 1:
    print("Paper")
    print(paper)
else:
    print("Scissors")
    print(scissors)

if computer_choice == 0 and choice == 1 or computer_choice == 1 and choice == 2 or computer_choice == 2 and choice == 0:
    print("You win!")
elif computer_choice == 0 and choice == 2 or computer_choice == 1 and choice == 0 or computer_choice == 2 and choice == 1:
    print("Computer wins!")
else:
    print("It's a draw!")
