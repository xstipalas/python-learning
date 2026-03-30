def good_vs_evil(good: str, evil: str) -> str:
    good_worth = [1, 2, 3, 3, 4, 10]
    evil_worth = [1, 2, 2, 2, 3, 5, 10]
    
    good_total = sum(int(count) * worth for count, worth in zip(good.split(), good_worth))
    evil_total = sum(int(count) * worth for count, worth in zip(evil.split(), evil_worth))
    
    result = (
        "Good triumphs over Evil",
        "Evil eradicates all trace of Good",
        "No victor on this battle field"
    )[
        0 if good_total > evil_total else
        1 if good_total < evil_total else
        2 
    ]

    return f'Battle Result: {result}'