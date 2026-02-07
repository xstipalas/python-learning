def tower_builder(n_floors):
    width = n_floors * 2 - 1
    result = []
    
    for i in range(n_floors):
        result.append(f'{"*" * (i * 2 + 1):^{width}}')
        
    return result
