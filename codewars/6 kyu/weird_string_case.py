def to_weird_case(words: str) -> str:
    return ' '.join(
        ''.join(
            letter.lower() if i & 1 else 
            letter.upper() 
            for i, letter in enumerate(word)
        )
        for word in words.split()
    )