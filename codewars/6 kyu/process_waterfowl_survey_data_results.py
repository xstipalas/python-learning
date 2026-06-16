import re

names_cache = {}
def encode_name(name: str) -> str:
    global names_cache
    
    if name in names_cache:
        return names_cache[name]
    
    words = re.split(r'[-\s]+', name)
    
    match len(words):
        case 1:
            code = words[0] if len(words[0]) <= 6 else words[0][:6]
        case 2:
            code = words[0][:3] + words[1][:3]
        case 3:
            code = words[0][:2] + words[1][:2] + words[2][:2]
        case 4:
            code = words[0][0] + words[1][0] + words[2][:2] + words[3][:2]
    
    names_cache[name] = code.upper()
    
    return names_cache[name]

def create_report(names: list[str]) -> list[str | int]:
    total = {}
    
    for name in names:
        duck_name, count = name.rsplit(maxsplit=1)
        
        if duck_name == "Labrador Duck":
            return ["Disqualified data"]
        
        duck_code = encode_name(duck_name)
        total[duck_code] = total.get(duck_code, 0) + int(count)
        
    return [item for pair in sorted(total.items()) for item in pair]
