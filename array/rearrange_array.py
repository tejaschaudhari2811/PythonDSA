def rearrange_array(arr):
    n = len(arr)
    min_index = 0
    max_index = n-1
    me = arr[n-1] + 1

    for i in range(n):
        if i % 2 == 0:
            arr[i] += (arr[max_index] % me) * me
            max_index -=1
        else:
            arr[i] += (arr[min_index] % me) * me
            min_index +=1

    for i in range(n):
        arr[i] = arr[i] // me

    return arr

print(rearrange_array([1,2,3,4,5]))