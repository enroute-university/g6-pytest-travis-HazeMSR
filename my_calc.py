def add(a,b):
    if not isinstance(a, (int, float)):
        raise Exception(f"Argument [{a}] must be a number")

    if not isinstance(b, (int, float)):
        raise Exception(f"Argument [{b}] must be a number")
    
    return a+b

def subs(a,b):
    if not isinstance(a, (int, float)):
        raise Exception(f"Argument [{a}] must be a number")

    if not isinstance(b, (int, float)):
        raise Exception(f"Argument [{b}] must be a number")

    return a-b

def mult(a,b):
    if not isinstance(a, (int, float)):
        raise Exception(f"Argument [{a}] must be a number")

    if not isinstance(b, (int, float)):
        raise Exception(f"Argument [{b}] must be a number")

    return a*b

def div(a,b):
    if not isinstance(a, (int, float)):
        raise Exception(f"Argument [{a}] must be a number")

    if not isinstance(b, (int, float)):
        raise Exception(f"Argument [{b}] must be a number")

    return a/b