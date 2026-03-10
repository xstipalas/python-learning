from typing import List

def wheat_from_chaff(vals: List[int]) -> List[int]:
    low, high = 0, len(vals) - 1
    
    while low < high:
        if vals[high] > 0:
            high -= 1
        elif vals[low] < 0:
            low += 1
        else:
            vals[low], vals[high] = vals[high], vals[low]
            
            low += 1
            high -= 1
            
    return vals