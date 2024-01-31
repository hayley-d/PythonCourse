student_heights = [151,145,179]
sum = 0
for height in student_heights:
  sum += height

average = round(sum/len(student_heights))

print(f"total height = {sum}")
print(f'number of students = {len(student_heights)}')
print(f'average height = {average}')