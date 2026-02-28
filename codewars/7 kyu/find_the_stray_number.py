def stray(arr):
    if arr[0] != arr[1]:
        return arr[0] if arr[1] == arr[2] else arr[1]
    
    default = arr[0]
    
    for i in range(2, len(arr)):
        if arr[i] != default:
            return arr[i]