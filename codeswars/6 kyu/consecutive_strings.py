def longest_consec(arr: list[str], k: int) -> str:
    n = len(arr)
    
    if n == 0 or k > n or k <= 0:
        return ''
    
    cur_len = sum([len(s) for s in arr[:k]])
    max_len = cur_len
    max_i = 0
    
    for i in range(k, n):
        cur_len += len(arr[i]) - len(arr[i - k])
        
        if cur_len > max_len:
            max_len = cur_len
            max_i = i - k + 1
    
    return ''.join(arr[max_i:max_i + k])
