line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

row = 0
col = 0;
if position[0] == 'A':
  row = 0
elif position[0] == 'B':
  row = 1
elif position[0] == 'C':
  row = 2

if position[1] == "1":
  col = 0
elif position[1] == "2":
  col = 1
elif position[1] == "3":
  col = 2

map[col][row] = "X"

print(f"{line1}\n{line2}\n{line3}")