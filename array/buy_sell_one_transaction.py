def buy_and_sell_one_transaction_brute(arr):
    # o(n^2)
    max_profit = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            max_profit = max(arr[j] - arr[i], max_profit)
    return max_profit

def buy_and_sell_optimized(arr):
    max_profit = 0
    prev_low = arr[0]
    for i in range(len(arr)):
        prev_low = min(prev_low, arr[i])
    
    print(prev_low)

print(buy_and_sell_optimized([7, 6, 4, 3, 1]))