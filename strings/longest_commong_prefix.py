# Longest common prefix

if __name__=="__main__":
    arr = ["geeksforgeeks","geek","geezer"]
    arr.sort()

    first = arr[0]
    last = arr[-1]
    minlen = min(len(first), len(last))
    i = 0
    while i < minlen and first[i] == last[i]:
        i +=1
    print(first[:i])
           