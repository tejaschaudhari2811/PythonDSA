def max_sum_subarray(arr):
    current_sum = 0
    max_sum = float('-inf') 
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_sum_subarray([-2, -4]))  
