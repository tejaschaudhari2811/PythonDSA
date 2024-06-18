def merge_arrays_without_extra_space(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i,j = 0,0
    for j in range(m):
        for i in range(n):
            if arr1[i] > arr2[j]:
                arr2[j],arr1[i] = arr1[i], arr2[j]
    arr2.sort()
    print(arr1, arr2)

merge_arrays_without_extra_space([10,12], [5,18,20])