def sign(x: float) -> int:
    return 1 if x > 0 else -1


def clamp(max_range: float, min_range: float, number: float) -> float:
    return max((min_range, min((number, max_range))))

def close_enough(var1: float, var2: float, max_variance: float = 0.0001) -> bool:
    return abs(var1-var2) < max_variance
