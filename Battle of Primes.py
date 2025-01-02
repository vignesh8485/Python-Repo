import math
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def min_warriors_to_kill(n1, n2):
    total = n1 + n2
    n3 = 1
    while True:
        if is_prime(total + n3):
            return n3
        n3 += 1
n1 = int(input())
n2 = int(input())
print(min_warriors_to_kill(n1, n2))
