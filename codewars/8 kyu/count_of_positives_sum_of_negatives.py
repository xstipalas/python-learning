from typing import List

def count_positives_sum_negatives(arr: List[int]) -> List[int]:
    if not arr:
        return []
    
    pos_count, neg_sum = 0, 0
    
    for num in arr:
        if num > 0:
            pos_count += 1
        else:
            neg_sum += num
            
    return [pos_count, neg_sum]