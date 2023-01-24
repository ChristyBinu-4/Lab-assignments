from time import sleep #Not so required
import numpy as np


def read_vector():
  print("Enter the values in vector : ")
  vector = [int(input(f'\t{v} =>')) for v in ['i', 'j', 'k']] #Reading i, j, k values into vector array 
  vector = np.array(vector)
  return vector

run = True
print("Axioms")
while run:
  print('''
        Enter any of the number to perform following command

        1. Associativity of Addition
        2. Commutativity of Addition
        3. Identity Element Of Addition
        4. Inverse Element Of Addition
        5. Distributrivity Of Scalar Multiplication Over Vector Addition
        6. Distributrivity Of Scalar Multiplication Over a Field Addition
        7. Compatibility Of Scalar Multiplication With Field Multiplication 
        8. Identity Element Of Scalar Multiplication

        9. Exit 
  ''')
  choice = int(input('Enter your choice => '))
  match(choice):
    case 1 :
      print('vector U : ')
      u = read_vector()

      print('vector V : ')
      v = read_vector()

      print('vector W : ')
      w = read_vector()

      print(f''' 
      (U + V) + W = {(u+v)+w}
      U + (V + W) = {u+(v+w)} 
      Therefore (U + V) + W = U + (V + W) 
      Hence proved
      ''')
      input("press Enter to continue")
    case 2 :
      print('vector U : ')
      u = read_vector()

      print('vector V : ')
      v = read_vector()

      print(f''' 
      (U + V) = {u+v}
      (V + U) = {v+u} 
      Therefore (U + V) = (V + U) 
      Hence proved
      ''')
      input("press Enter to continue")
    case 3 :
      print('vector V : ')
      v = read_vector()

      print(f''' 
      V + I = {v+0}
      I is the identity element which is 0

      Therefore V + I = V
      Hence proved
      ''')
      input("press Enter to continue")
    case 4 :

      print('vector V : ')
      v = read_vector()

      print(f''' 
      V + -V = {v+(-v)}
      -V is the inverse element of V

      Therefore V + -V = 0
      Hence proved
      ''')     
      input("press Enter to continue")

    case 5 :
      print('vector U : ')
      u = read_vector()

      print('vector V : ')
      v = read_vector()

      scalarValue = int(input('Enter the scalar value : '))

      print(f''' 
      C * (U + V) = {scalarValue*(u+v)}
      (U * C) + (V * C) = {(u * scalarValue) + (v *scalarValue)}

      Therefore C * (U + V) = (U * C) + (V * C) 
      Hence proved
      ''')           
      input("press Enter to continue")

    case 6 :
      print('vector V : ')
      v = read_vector()

      scalarValue1 = int(input('Enter the scalar value : '))      
      scalarValue2 = int(input('Enter the scalar value : '))

      print(f''' 
      (C1 + C2) * V = {(scalarValue1 + scalarValue2) * v}
      (C1 * V) + (C2 * V) = {(scalarValue1 * v) + (scalarValue2 * v)}

      Therefore (C1 + C2) * V =  (C1 * V) + (C2 * V)
      Hence proved
      ''')     
      input("press Enter to continue")

    case 7 :
      print('vector V : ')
      v = read_vector()

      scalarValue1 = int(input('Enter the scalar value : '))      
      scalarValue2 = int(input('Enter the scalar value : '))

      print(f''' 
      C1 * (C2 * V) = {scalarValue1 * (scalarValue2 * v)}
      (C1 * C2) * V = {(scalarValue1 + scalarValue2) * v}

      Therefore C1 * (C2 * V) =  (C1 * C2) * V
      Hence proved
      ''')     

    case 8 :
      print('vector V : ')
      v = read_vector()

      print(f''' 
      V * I = {v * 1}

      Here V * I = V, 1 is the multiplicative identity of a vector 
      Axiom proved
      ''')  
      input("press Enter to continue")

    case 9 :
      print("Quiting...")
      sleep(2)#Code is not required
      run = False
    
    case _ :
      print("Invalid entry try again..")
      input('press enter to continue..')
