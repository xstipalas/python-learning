import math

def prob_simpson(lamb: int, x: int, op='=') -> float:
    match op:
        case '=':
            return lamb ** x * math.exp(-lamb) / math.factorial(x)
        case '>':
            return sum(prob_simpson(lamb, i) for i in range(x))
        case '>=':
            return prob_simpson(lamb, x, '>') + prob_simpson(lamb, x)
        case '<':
            return 1 - prob_simpson(lamb, x, '>=')
        case '<=':
            return 1 - prob_simpson(lamb, x, '>')