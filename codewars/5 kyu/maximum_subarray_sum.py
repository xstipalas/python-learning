def max_sequence(arr):
    cur_max = 0
    max_sum = 0
    
    for i in range(len(arr)):
        cur_max = max(0, cur_max + arr[i])
        max_sum = max(cur_max, max_sum)
        
    return max_sum
            
        
