def get_indices(arr, expected_sum, n):
    for i in range(n):
        sum = arr[i]
        for j in range(i+1,n):
            sum += arr[j]
            if sum > expected_sum:
                break
            elif sum == expected_sum:
                return i,j
    
def get_indices_optimum(arr, expected_sum, n):
    # Effcieint approach sliding window
    current_sum = arr[0]
    start = 0
    i = 1
    while i<=n:
        while current_sum > expected_sum and start < i-1:
            current_sum = current_sum - arr[start]
            start +=1
        
        if current_sum == expected_sum:
            print(start, i-1)
            return 1
        if i<n:
            current_sum += arr[i]
        i+=1
    print("No subarray found")
    return -1 





print(get_indices_optimum([1,2,3,4,5,6,7,8,9,10], 15, 10))
