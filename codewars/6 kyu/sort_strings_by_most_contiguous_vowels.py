def sort_strings_by_vowels(seq: list[str]) -> list[str]: 
    def longest_sub(s):
        abc = 'aeiouAEIOU'
        count = 0
        max_count = 0
        
        for ch in s:
            if ch in abc:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 0
                
        return max_count
    
    return sorted(seq, key=longest_sub, reverse=True)