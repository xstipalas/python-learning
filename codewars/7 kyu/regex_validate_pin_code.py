def validate_pin(pin: str) -> bool:
    return pin.isdigit() and len(pin) in (4, 6)