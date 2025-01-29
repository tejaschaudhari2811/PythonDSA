def plus_one(arr):
    i = len(arr) - 1
    carry = 1
    while i >=0:
        if arr[i] + carry > 9:
            arr[i] = 0
            carry = 1
        else:
            arr[i] +=1
            carry = 0 
            break
        i-=1
    if carry:
        arr.insert(0, carry)
    
    return arr

print(plus_one([9,9,9]))