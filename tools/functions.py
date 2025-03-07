def is_prime(n):
    divs = [i for i in range(1, n + 1) if n % i == 0]
    if len(divs) == 2:
        return True
    else:
        return False
