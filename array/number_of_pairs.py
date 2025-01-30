def find_number_of_pairs(arr1, arr2):
    m, n = len(arr1), len(arr2)
    pairs = 0
    for i in range(m):
        for j in range(n):
            if arr1[i]**arr2[j] > arr2[j]**arr1[i]:
                pairs +=1
    
    return pairs

print(find_number_of_pairs([2,3,4,5],[1,2,3]))