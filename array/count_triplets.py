def count_triplets_on3(arr, n):
    triplets = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] in arr:
                triplets +=1
    return triplets

def count_triplets_on2(arr, n):
    freq = [0] * 10**5
    for ele in arr:
        freq[ele] +=1
    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (freq[arr[i]+arr[j]]):
                count +=1
    return count

print(count_triplets_on2([1, 5, 3, 2], 4))