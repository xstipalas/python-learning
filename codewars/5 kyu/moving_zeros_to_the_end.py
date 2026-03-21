def move_zeros(lst: list[int]) -> list[int]:
    left = 0
    
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[i], lst[left] = lst[left], lst[i]
            left += 1
            
    return lst