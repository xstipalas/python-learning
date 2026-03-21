def to_camel_case(text: str) -> str:
    result = []
    flag = False
    
    for ch in text:
        if ch.isalpha():
            if flag:
                result.append(ch.upper())
                flag = False
            else:
                result.append(ch)
        else:
            flag = True
            
    return ''.join(result)
            