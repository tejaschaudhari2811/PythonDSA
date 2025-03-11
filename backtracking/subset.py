def generate_subsets(arr):
    n = len(arr)

    res, sol = [] , []

    def backtrack(i):
        if i == n:
            res.append(sol[:])
            return
        
        backtrack(i+1)

        sol.append(arr[i])
        backtrack(i+1)
        sol.pop()

    backtrack(0)

    return res

print(generate_subsets([1,2,3]))