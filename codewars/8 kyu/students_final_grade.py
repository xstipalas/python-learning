def final_grade(exam: int, projects: int) -> int:
    return (0, 75, 90, 100)[3 if exam > 90 or projects > 10 else
                           2 if exam > 75 and projects >= 5 else
                           1 if exam > 50 and projects >= 2 else 
                           0]