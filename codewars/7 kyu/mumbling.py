def accum(st):
    result = [ch.upper() + (ch.lower() * i) for i, ch in enumerate(st)]
    
    return '-'.join(result)