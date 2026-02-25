import re

def solution(s):
    words = re.findall(r'[A-Z][a-z]*|[a-z]+', s)
    return ' '.join(words)
