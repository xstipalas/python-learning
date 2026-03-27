def ips_between(start: str, end: str) -> int:
    a, b, c, d = (int(y) - int(x) for x, y in zip(start.split('.'), end.split('.')))
    
    return ((a * 256 + b) * 256 + c) * 256 + d