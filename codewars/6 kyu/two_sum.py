def two_sum(numbers, target):
    hash = {}
    
    for i, num in enumerate(numbers):
        needed = target - num
        
        if needed in hash:
            return hash[needed], i
        else:
            hash[num] = i
                