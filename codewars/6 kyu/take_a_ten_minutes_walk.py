def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    x = y = 0
    
    for side in walk:
        match side:
            case 'w': x += 1
            case 'e': x -= 1
            case 'n': y += 1
            case 's': y -= 1
                
    return x == y == 0