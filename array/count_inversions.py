def count_inversions_to_sort(arr):
    new_arr = sorted(arr) # O(nlogn)
    mismatches = 0
    for i in range(len(arr)): #(o(n))
        if new_arr[i] != arr[i]:
            mismatches +=1
    
    return mismatches -1

print(count_inversions_to_sort([2,4,1,3,5]))