def odd_or_even(arr):
    return ('odd', 'even')[sum(arr) & 1 == 0]