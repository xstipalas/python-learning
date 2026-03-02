def bouncing_ball(h: int, bounce: float, window: int) -> int:
    result = -1
    
    if h < 0 or not 0 < bounce < 1 or window >= h:
        return result
    
    while h > window:
        result += 2
        h *= bounce
        
    return result