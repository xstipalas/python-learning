def enough(cap: int, on: int, wait: int) -> int:
    return 0 if cap > on + wait else on + wait - cap