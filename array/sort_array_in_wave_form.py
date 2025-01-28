def sort_array_in_wave(arr):
    n = len(arr)
    for i in range(0,n,2):

        if (i > 0 and arr[i] < arr[i-1]):
            arr[i], arr[i-1] = arr[i-1], arr[i]

        if (i < n-1 and arr[i] < arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return arr

print(sort_array_in_wave([10, 90, 49, 2, 1, 5, 23]))