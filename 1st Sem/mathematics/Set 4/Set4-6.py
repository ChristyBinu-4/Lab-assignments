#Question 6: Perform basic string operations
i = True
while i == True :
  print('''
        Enter any of the number to perform following command

        1. Concatenation
        2. Upper Case
        3. Lower Case
        4. Capitalize 
        5. Find string length
        6. Replace
        7. Index of specific word

        8. Exit 
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

    case 5 :
      print("Length of the word\n")
      a = input("Enter any characters : ")   
      print(f"Result : {len(a)}")
      input("Press Enter to continue")

    case 6 :
      print("Replacing word\n")
      a = input("Enter any characters : ")
      b = input("Enter the text to be changed : ")   
      c = input("Enter the text to be replaced : ")   
      print(f"Result of after replacing : {a.replace(b, c)}")
      input("Press Enter to continue")

    case 7 :
      print("Index of word\n")
      a = input("Enter any characters : ")
      b = input("Enter the text to find from above string : ")      
      print(f"Your string is at position : {a.index(b)}")
      input("Press Enter to continue")

    case 8 :
      i = False
