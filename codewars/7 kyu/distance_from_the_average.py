def distances_from_average(test_list: list[int | float]) -> list[float]:
    mean = sum(test_list) / len(test_list)
    
    return [round(mean - x, 2) for x in test_list]