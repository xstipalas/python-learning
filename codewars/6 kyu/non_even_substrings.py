def solve(s: str) -> int:
    return sum(i for i, num in enumerate(s, 1) if int(num) & 1 == 1)