import bisect

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    return primes

def min_absolute_difference(N, primes):
    if N in primes:
        return 0
    
    pos = bisect.bisect_left(primes, N)
    
    prime_below = primes[pos - 1] if pos > 0 else float('inf')
    prime_above = primes[pos] if pos < len(primes) else float('inf')
    
    diff_below = abs(N - prime_below) if prime_below != float('inf') else float('inf')
    diff_above = abs(N - prime_above) if prime_above != float('inf') else float('inf')
    
    return min(diff_below, diff_above)

import sys
input = sys.stdin.read
data = input().splitlines()

limit = 10**6
primes = sieve(limit)

results = []

for line in data:
    N = int(line)
    results.append(str(min_absolute_difference(N, primes)))

sys.stdout.write("\n".join(results) + "\n")
