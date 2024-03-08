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
    


array = [4, 5, 9, 8, 32, 1, 43, 54, 23, 53, 28, 10, 30, 80, 23]
array = sorted(array)
key = 54 #key is the element to be found from the array
print("\n sorted array is ",array)

searchResult = binarySearch(array, key) + 1 #adding 1 to make the postion of array start from 1

if searchResult == None:
  print('element is not found')
else:
  print(f'\n {key} is found at {searchResult}th position')