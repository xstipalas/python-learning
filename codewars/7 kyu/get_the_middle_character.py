def get_middle(s):
    n = len(s)
    mid = n // 2
    
    if n <= 2:
        return s
    
    if n % 2 == 0:
        return s[mid - 1: mid + 1]
    else:
        return s[mid]