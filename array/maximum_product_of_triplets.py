from typing import List

#1 Three nested loops
#2 Sorting
#3 Using heaps

#1
def get_triplets_product(arr: List) -> int:
    max_product = float("-inf")
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                curr_product = arr[i] * arr[j] * arr[k]
                max_product = max(max_product, curr_product)
    return max_product

if __name__=="__main__":
    print(get_triplets_product([10, 3, 5, 6, 20]))