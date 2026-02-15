def sort_array(source_array):
    odd_nums = sorted(num for num in source_array if num % 2 == 1)
    cur_i = 0
    
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = odd_nums[cur_i]
            cur_i += 1
            
    return source_array