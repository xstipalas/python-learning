def count(s):
    count_dict = {}
    
    for ch in s:
        count_dict[ch] = count_dict.get(ch, 0) + 1
        
    return count_dict