def increment_string(string: str) -> str:
    if not string:
        return '1'
    
    i = len(string) - 1
    
    while string[i].isdigit() and i >= 0:
        i -= 1
        
    str_part, num_part = string[:i + 1], int(string[i + 1:] or 0) + 1
    x = len(string) - i - 1
    
    return f'{str_part}{num_part:0{x}}'
