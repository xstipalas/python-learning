from typing import List

def capitalize(s: str) -> List[str]:
    result = ''.join(ch.upper() if i & 1 == 0 else ch for i, ch in enumerate(s))
    
    return [result, result.swapcase()]