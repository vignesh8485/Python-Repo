def is_pronic_number(X):
    x = 0
    while x * (x + 1) <= X:
        if x * (x + 1) == X:
            return "YES"
        x += 1
    return "NO"

X = int(input())
print(is_pronic_number(X))
