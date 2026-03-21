def generate_hashtag(s: str) -> str:
    if not s:
        return False
    
    res = '#' + ''.join(s.title().split())
    
    if len(res) > 140:
        return False
    
    return res
