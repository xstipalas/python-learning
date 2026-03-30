def parts_sums(ls: list[int]) -> list[int]:
    result = [0]
    
    for i in range(len(ls) - 1, -1, -1):
        result.append(result[-1] + ls[i])
        
    return result[::-1]