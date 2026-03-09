from typing import List

def min_max(lst: List[int]) -> List[int]:
    min_val = max_val = lst[0]
    
    for val in lst:
        if val > max_val:
            max_val = val
        elif val < min_val:
            min_val = val
            
    return [min_val, max_val]
