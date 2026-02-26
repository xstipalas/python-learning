from typing import List

def dir_reduc(arr: List[str]) -> List[str]:
    '''Оптимизация маршрута, удаляя противоположные направления.'''

    opposites = {
        'NORTH': 'SOUTH', 'SOUTH': 'NORTH',
        'EAST': 'WEST', 'WEST': 'EAST',
    }
    
    result = []
    
    for side in arr:
        if result and result[-1] == opposites[side]:
            result.pop()
        else:
            result.append(side)
    
    return result