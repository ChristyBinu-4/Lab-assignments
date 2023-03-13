#Question 3: Sort elements of an array


def sort(array):
  length = len(array)
  for i in range(length):
    minimum  = array[i]
    position = i

    for j in range(i + 1, length):

      if(array[j] < minimum):
        minimum = array[j]
        position = j
    
    if position != i :
      array[position] = array[i]
      array[i] = minimum
  
  return array


print("\nSorting Arrays\n")

no_of_elements = int(input("Enter the number of elements in array to be sorted : "))
print("\nEnter the elements in array : ")
array = [int(input("=>")) for i in range(no_of_elements)]

print("Input array is : ", array)
sorted_array = sort(array)
print("Sorted array is : ", sorted_array)