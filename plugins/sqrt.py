name = "sqrt"

def run(num1, _):
    if num1 < 0:
        raise ValueError("Cannot take square root of negative number")
    return num1 ** 0.5

