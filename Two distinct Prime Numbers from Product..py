def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def find_prime_pair(N, is_prime):
    for p1 in range(2, int(N**0.5) + 1):
        if is_prime[p1] and N % p1 == 0:
            p2 = N // p1
            if p2 != p1 and is_prime[p2]:
                return p1, p2
    return -1
limit = 1000000
is_prime = sieve(limit)
N = int(input().strip())
result = find_prime_pair(N, is_prime)

if result == -1:
    print(result)
else:
    print(result[0], result[1])
