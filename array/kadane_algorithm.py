# For the given array find the subarray with maximum sum
def max_sum_subarray(arr, n):
    current_sum = arr[0]
    max = current_sum
    for i in range(1,n):
        current_sum += arr[i]
        if current_sum > max:
            max = current_sum
    return max

print(max_sum_subarray([5,4,7],3))