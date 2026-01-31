import re

def order(sentence):
    words = sorted(sentence.split(), key=lambda x: int(re.sub(r'\D', '', x)))
            
    return ' '.join(words)
