import math  # Don't forget to import the math module
def paint_calc(height,width,cover):
  num_cans = int(math.ceil((height*width)/cover))
  print(f"You'll need {num_cans} cans of paint.")
# Define a function called paint_calc() so the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)