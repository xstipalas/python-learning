from preloaded import LOVE_LANGUAGES as LL 

def love_language(partner, weeks): 
    n = weeks * 7 // 5 
    results = {word: sum(
        1 for _ in range(n) if partner.response(word) == 'positive') 
            for word in LL} 
        
    return max(results, key=lambda x: results[x])