from typing import List

def points(games: List[str]) -> int:
    score = 0
    
    for game in games:
        x, y = game[0], game[-1]
        
        if x > y:
            score += 3
        elif x == y:
            score += 1
            
    return score