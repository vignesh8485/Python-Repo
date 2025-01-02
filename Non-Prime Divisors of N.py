import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def count_non_prime_divisors(N):
    divisors = set()
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            divisors.add(i)
            if i != N // i:
                divisors.add(N // i)
    non_prime_count = 0
    for divisor in divisors:
        if not is_prime(divisor):
            non_prime_count += 1

    return non_prime_count
N = int(input())
print(count_non_prime_divisors(N))
