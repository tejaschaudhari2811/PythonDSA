# This script aims to learn how to declare array in python
import array

# Declare a static array
arr = array.array("i", [1,2,3,4,5,0])




# Insert element
def insert(arr, new_element, position, n):
    for i in range(n-1, position-1, -1):
        arr[i+1] = arr[i]
    arr[position] = new_element
    
    
insert(arr, 10, 2, 5)

# Array Traversal
for element in arr:
    print(element, end=" ")