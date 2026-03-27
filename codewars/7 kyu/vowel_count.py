def get_count(sentence: str) -> int:
    return sum(1 for ch in sentence if ch in {'a', 'e', 'i', 'o', 'u'})