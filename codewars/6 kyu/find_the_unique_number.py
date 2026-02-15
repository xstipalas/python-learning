def find_uniq(arr):
    if arr[0] == arr[1]:
        equal = arr[0]
    elif arr[1] == arr[2]:
        return arr[0]
    else:
        return arr[1]
    
    for el in arr:
        if el != equal:
            return el
