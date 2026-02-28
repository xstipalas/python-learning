from typing import List

def sum_dig_pow(a: int, b: int) -> List[int]:
    result = []
    
    for num in range(a, b + 1):
        if sum(int(x) ** i for i, x in enumerate(str(num), 1)) == num:
            result.append(num)
            
    return result