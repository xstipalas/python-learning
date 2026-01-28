def get_pins(observed):
    '''Поиск всех возможных пинкодов'''
    possible_nums = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }
    
    result = ['']
    
    for digit in observed:
        temp = []
        for prefix in result:
            for variant in possible_nums[digit]:
                temp.append(prefix + variant)
        
        result = temp
        
    return result
