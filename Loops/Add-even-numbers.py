target = int(input()) # Enter a number between 0 and 1000
count = 0

if target > count:
  for num in range(1,target+1):
    if num%2 == 0:
      count += num

print(count)