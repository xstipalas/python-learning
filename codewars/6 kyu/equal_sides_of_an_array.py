def find_even_index(arr):
    if not arr:
        return -1
    
    left_sum, total = 0, sum(arr)
    i = 0
    
    for i, num in enumerate(arr):
        if left_sum == total - left_sum - num:
            return i
        
        left_sum += num
    
    return -1