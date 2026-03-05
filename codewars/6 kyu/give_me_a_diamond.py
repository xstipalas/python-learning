def diamond(n: int) -> str:
    if n <= 0 or n & 1 == 0:
        return None
    
    diamond = []
    stars = 1
    spaces = n // 2
    
    while stars < n:
        diamond.append(' ' * spaces + '*' * stars + '\n')
        
        stars += 2
        spaces -= 1
        
    while stars > 0:
        diamond.append(' ' * spaces + '*' * stars + '\n')
        
        stars -= 2
        spaces += 1
        
    return ''.join(diamond)
    