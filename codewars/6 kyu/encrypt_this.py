def encrypt_word(word):
    if len(word) < 2:
        return str(ord(word))
    
    word = list(word)
    word[0] = str(ord(word[0]))
    word[1], word[-1] = word[-1], word[1]
    
    return ''.join(word)

def encrypt_this(text):
    if not text:
        return text
    
    encrypt_words = map(encrypt_word, text.split())
    
    return ' '.join(encrypt_words)
