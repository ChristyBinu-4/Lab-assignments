#Question 1: Armstrong or not


def armstrong_or_not(number):
  temperoryNumber = number
  sum = 0
  while temperoryNumber:
    digit = temperoryNumber % 10
    sum += digit ** 3
    temperoryNumber //= 10
  if sum == number :
    return True
  return False


print("ARMSTRONG OR NOT", end="\n\n")

number = int(input("Enter the number to be checked : "))
check = armstrong_or_not(number)

if check:
  print("The given number is an armstrong number")
else :
  print("The given number is not an armstrong number")