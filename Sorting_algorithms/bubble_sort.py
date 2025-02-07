def sort(arr):
    n = len(arr)
    swap = True
    for i in range(n-1):
        for j in range(i, n):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            else:
                swap = False

            if not swap:
                continue

    print(arr)

sort([5,4,3,2,1])