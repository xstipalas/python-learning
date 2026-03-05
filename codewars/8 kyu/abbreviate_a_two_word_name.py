def abbrev_name(name: str) -> str:
    first, last = name.split()
    
    return f'{first[0].upper()}.{last[0].upper()}'