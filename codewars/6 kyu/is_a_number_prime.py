def is_prime(num: int) -> bool:
    if num == 2:
        return True
    
    if (
        num < 0 or
        num < 2 or
        num & 1 == 0
        ):
        return False
    
    for div in range(3, int(num ** 0.5) + 1, 2):
        if num % div == 0:
            return False
        
    return True
    