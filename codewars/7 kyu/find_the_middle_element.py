def gimme(arr):
    max_i = min_i = 0
    
    for i, num in enumerate(arr):
        if num > arr[max_i]:
            max_i = i
        elif num < arr[min_i]:
            min_i = i
            
    return 3 - max_i - min_i
    