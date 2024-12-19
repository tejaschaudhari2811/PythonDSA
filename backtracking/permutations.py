def get_permutations(arr):
    res = []

    def dfs(index):
        if index == len(arr):
            res.append(arr.copy())
            return
        for i in range(index, len(arr)):
            arr[i], arr[index] = arr[index], arr[i]
            dfs(index + 1)
            arr[i], arr[index] = arr[index], arr[i]
    dfs(0)
    return res


if __name__=="__main__":
    result = get_permutations([1,2,3])
    print(result)