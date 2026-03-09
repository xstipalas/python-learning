from typing import List

def frame(text: List[str], char: str) -> str:
    max_len = max(len(line) for line in text)    
    border = char * (max_len + 4)
    result = [border]
    
    for line in text:
        result.append(f'{char} {line:<{max_len}} {char}')
        
    result.append(border)
    
    return '\n'.join(result)
    