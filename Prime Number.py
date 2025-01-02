import math
def is_prime(N):
    if N <= 1:
        return False
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True
N = int(input().strip())
if is_prime(N):
    print("Prime")
else:
    print("Not a Prime")
