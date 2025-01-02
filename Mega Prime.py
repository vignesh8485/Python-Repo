def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def is_mega_prime(N, is_prime):
    if not is_prime[N]:
        return "Not Mega Prime"
    prime_digits = {'2', '3', '5', '7'}
    for digit in str(N):
        if digit not in prime_digits:
            return "Not Mega Prime"
    
    return "Mega Prime"
limit = 1000000
is_prime = sieve(limit)
N = int(input().strip())
print(is_mega_prime(N, is_prime))
