def count_consecutive_ones(arr):
    max = 0
    for i in range(len(arr)):
        first, second = i,i
        while arr[second] != 0:
            second +=1
        max = max(max, second - first+1)
    return max