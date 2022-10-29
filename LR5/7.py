def isPrime(num, x = 2):
    if num < x * x:
        return True
    if num % x == 0:
        return False
    return isPrime(num, x + 1)
