def seq_to_one(n: int) -> list[int]:
    return list(range(n, 2) if n <= 1 else range(n, 0, -1))