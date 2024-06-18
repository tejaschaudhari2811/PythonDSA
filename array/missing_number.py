# Given an array of size n-1 and therefore surely one number is missing
# Following approach only works for some solutions but not all. It will work if the arry is sorted.
def get_missing_number(arr, n):
    arr.sort() #o(nlogn)
    if len(arr) == 1 and n > 1:
        return n
    for i in range(1, n): #o(n)
        if arr[i-1] != i:
            return i

def get_missing_number_auxilary_array(arr):
    n = len(arr)
    temp = [0] * (n+1)

    for i in range(0,n):
        temp[arr[i]-1] = 1
    
    for i in range(0,n+1):
        if temp[i] == 0:
            return i+1
        

def get_missing_number_natural_sum(arr, n):
    sum_of_n = n * (n+1)/2
    array_sum = sum(arr)
    return sum_of_n - array_sum

print(get_missing_number_natural_sum([1, 2, 4, 6, 3, 7, 8], 8))