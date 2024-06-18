def count_triplets(arr, n):
    triplets = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] in arr:
                triplets +=1
    return triplets

print(count_triplets([2,3,4], 3))