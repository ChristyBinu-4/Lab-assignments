#Question 6: Perform basic string operations
i = True
while i == True :
  print('''
        Enter any of the number to perform following command

        1. Concatenation
        2. Upper Case
        3. Lower Case
        4. Capitalize 
        5. Right Strip
        6. Left Strip

        7. Exit 
  ''')
  choice = int(input())
  match(choice):
    case 1 : 
      print("Concatenation \n")
      a = input("Enter the first characters : ")
      b = input("Enter the Second characters : ")
      print(f"Result : {a+b}")
      input("Press Enter to continue")

    case 2 :
      print("Upper case \n")
      a = input("Enter any characters : ")
      print(f"Result : {a.upper()}")
      input("Press Enter to continue")

    case 3 :
      print("Lower case \n")
      a = input("Enter any characters : ")
      print(f"Result : {a.lower()}")
      input("Press Enter to continue")

    case 4 :
      print("Capitalize the word\n")
      a = input("Enter any characters : ")
      print(f"Result : {a.capitalize()}")
      input("Press Enter to continue")

    case 7 :
      i = False
