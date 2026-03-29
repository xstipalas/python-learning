def parse(data: str) -> list[int]:
    value = 0
    result = []
    
    for command in data:
        match command:
            case 'i':
                value += 1
            case 'd':
                value -= 1
            case 's':
                value **= 2
            case 'o':
                result.append(value)
                
    return result