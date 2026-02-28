def expanded_form(num):
    num_str = str(num)
    n = len(num_str)
    
    result = [dig + '0' * (n - i) for i, dig in enumerate(num_str, 1) if dig != '0']
    
    return ' + '.join(result)