#Question 4: Binary Search

def binarySearch(array, key):
  firstElement = 0
  lastElement = len(array) -1 # last element = length of array -1
  
  while lastElement >= firstElement : 
    middleElement = int((firstElement+lastElement)/2)
    
    if array[middleElement] == key:
      return middleElement
    elif array[middleElement] > key:
      lastElement = middleElement - 1 
    elif array[middleElement] < key :
      firstElement = middleElement + 1
  return
    
#Inputing the elements in array
length = int(input("Enter the Number of elements you want to input in an array : "))
print("Enter the elements in array")
array = [int(input(">")) for i in range(length)]

array = sorted(array)
key = int(input("Enter the element to be searched : "))

searchResult = binarySearch(array, key) + 1 #adding 1 to make the postion of array start from 1

if searchResult == None:
  print('element is not found')
else:
  print(f'\n {key} is found at {searchResult}th position')