def chromosome_check(chromosome: str) -> str:
    return f"Congratulations! You\'re going to have a {('son', 'daughter')[chromosome[1] == 'X']}."
