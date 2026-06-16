def histogram(values, bin_width):
    if not values:
        return []
    
    counter = {i: 0 for i in range(max(values) // bin_width + 1)}
    
    for num in values:
        ind = num // bin_width
        counter[ind] += 1
        
    return [counter[ind] for ind in sorted(counter.keys())]
