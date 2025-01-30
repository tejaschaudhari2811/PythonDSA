def sort_array_using_selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(sort_array_using_selection_sort([64, 25, 12, 22, 11]))