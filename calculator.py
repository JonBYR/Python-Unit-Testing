import math
def is_prime(num):
    if type(num) != int:
        raise TypeError('num is of invalid type')
    if num < 0:
        raise ValueError('Check if the value of num is not negative')
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def add(a,b):
    return a + b