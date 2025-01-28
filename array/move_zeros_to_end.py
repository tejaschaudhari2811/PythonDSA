def move_zeros_to_end(arr):
    count = 0
    new_arr = [] #O(n)
    for num in arr: #O(n)
        if num == 0:
            count +=1
        else:
            new_arr.append(num)
    new_arr.extend([0]*count)
    print(new_arr)

def move_to_end(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            
            arr[count], arr[i] = arr[i], arr[count]
            count +=1
            
    print(arr)
    return arr


move_to_end([1, 2, 0, 4, 3, 0, 5, 0])
    