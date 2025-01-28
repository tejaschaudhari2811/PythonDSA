def rotate_array(arr, d):
    # 1. Take an extra array, add elements from d to n-1 to the array and then add
    # 0 to d-1 elements to the array at the end
    # 2. Reversal Algorithm
    # 3. Juggling Algorithm
    n = len(arr)
    if n < d:
        d = d%n
    left = 0
    right = d - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1
    
    left = d
    right = n-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1

    left = 0
    right = n-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1
    
    return arr

print(rotate_array([1, 2, 3, 4, 5, 6], 2))
    
