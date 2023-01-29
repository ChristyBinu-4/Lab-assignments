#Question 2: Merge sort 

def merge_sort(array):
    if len(array) > 1:
      mid = len(array)//2

      left = array[:mid]
      right = array[mid:]

      merge_sort(left)
      merge_sort(right)

      i = k = j = 0

      while i < len(left) and j < len(right):
        if left[i] < right[j]:
          array[k] = left[i]
          i += 1
        else:
          array[k]  = right[j]
          j += 1
        k += 1

      while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
      
      while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1    

      return array

length = int(input("How many elements should be inputed?\n"))
print("Enter the elements in array : ")
array = [int(input("=>")) for i in range(length)]
print(merge_sort(array))



