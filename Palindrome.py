def is_palindrome(n):
    num_str = str(n)
    return num_str == num_str[::-1]
n = int(input())
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")
