def is_disarium(n):
    digits = str(n)
    total = 0
    for i, digit in enumerate(digits, 1):
        total += int(digit) ** i
    return total == n
n = int(input())
if is_disarium(n):
    print("True")
else:
    print("False")
