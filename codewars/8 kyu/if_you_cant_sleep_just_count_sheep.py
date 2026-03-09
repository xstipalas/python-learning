def count_sheep(n: int) -> str:
    return ''.join(f'{i} sheep...' for i in range(1, n + 1))