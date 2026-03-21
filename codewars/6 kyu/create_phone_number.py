def create_phone_number(n: list[int]) -> str:
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)