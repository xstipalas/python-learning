def color_probability(color: str, texture: str) -> str:
    MARBLES = {
        'smooth': {
            'red': 1,
            'yellow': 1,
            'green': 1,
        },
        'bumpy': {
            'red': 4,
            'yellow': 2,
            'green': 1,
        },
    }
    
    return str(MARBLES[texture][color] / sum(MARBLES[texture].values()))[:4]