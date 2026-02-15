def duplicate_encode(word):
    word = word.lower()
    letters_count = {}
    result = []
    
    for l in word:
        letters_count[l] = letters_count.get(l, 0) + 1
        
    for l in word:
        new_l = '(' if letters_count[l] == 1 else ')'
        
        result.append(new_l)
        
    return ''.join(result)
