def added_char(s1: str, s2: str) -> str:
    result = 0
    
    for ch in s1 + s2:
        result ^= ord(ch)
        
    return chr(result)