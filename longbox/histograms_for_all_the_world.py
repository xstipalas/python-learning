from math import ceil, log

def hist_maker(students_results):
    result = []
    
    students_results.sort()
    
    n = len(students_results)
    
    _min = students_results[0]
    _max = students_results[-1]
    
    _range = _max - _min
    
    k = int(1 + 3.32 * log(n, 10))
    
    A = ceil(_range / k)
    
    bounds = [[_min + i * A, _min - 1 + (i + 1) * A] if i < k - 1 else 
              [_min + i * A, min(_min + (i + 1) * A, 100)] for i in range(k)]
    
    Fa = 0
    cur_i = 0
    for num in range(k):
        F = 0
        while cur_i < n and students_results[cur_i] <= bounds[num][1]:
            F += 1
            cur_i += 1
        Fa += F
        
        result.append([num + 1, bounds[num], F, Fa])
        
    return result
