#Question 1: Insertion sort 


def insertion_sort(array):
  length = len(array)

  for i in range(1, length):
    key = array[i]
    j = i 
     
    while j > 0 and key < array[j - 1]:
      array[j] = array[j - 1]
      j -= 1
    array[j] = key
  return array

length = int(input("How many elements should be inputed?\n"))
print("Enter the elements in array : ")
arr = [int(input("=>")) for i in range(length)]
print(insertion_sort(arr))
