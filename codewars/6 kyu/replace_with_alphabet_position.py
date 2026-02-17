import string

def alphabet_position(text: str) -> str:
    abc = {ch: str(order) for order, ch in enumerate(string.ascii_lowercase, start=1)}
    
    return ' '.join(abc[ch] for ch in text.lower() if 'a' <= ch <= 'z')