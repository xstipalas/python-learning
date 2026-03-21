def multiplication_table(size: int) -> list[int]:
    return [[(j + 1) * (i + 1) for j in range(size)] for i in range(size)]