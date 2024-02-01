def prime_checker(number):
  i = 2
  while not i == number:
    if number % i == 0:
      print("It's not a prime number.")
      return
    i +=1
  print("It's a prime number.")