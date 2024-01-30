import random
names_string = ["Hayley","Dom","Eevee","Tessa","Harry","Milly"]
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
random_index = random.randint(0,len(names)-1)

print(f"{names[random_index]} is going to buy the meal today!")