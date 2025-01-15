# Find the second largest element in an array
#1. Sorting and return index 1 or -2
#2. Go through array and find second largest in two passes
#3. Go through the array and find the second largest in one pass
from typing import List

#3
def find_second_largest(arr: List) -> int:
    first, second = 0, 0 
    for item in arr:
        if item > first:
            second = first
            first = item
        elif item < first and item > second:
            second = item

    return second

if __name__=="__main__":
    arr = [1,2,4,5,10,22]

    print(find_second_largest(arr))