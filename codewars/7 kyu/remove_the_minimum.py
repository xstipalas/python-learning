import math
from typing import List

def remove_smallest(numbers: List[int]) -> List[int]:
    min_i = 0
    min_rating = math.inf
    
    for i, rating in enumerate(numbers):
        if rating < min_rating:
            min_i = i
            min_rating = rating
    
    return numbers[:min_i] + numbers[min_i + 1:]