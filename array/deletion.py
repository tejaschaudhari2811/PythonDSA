import array

arr = array.array("i",[1,2,3,4,10,5])

def find_element(element, arr):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

def delete_element(arr, element, n):
    pos = find_element(element, arr)
    if pos < 0:
        return
    else:
        for i in range(pos, n-1):
            arr[i] = arr[i+1]
    

delete_element(arr, 10, 6)

# Array Traversal
for element in arr:
    print(element, end=" ")