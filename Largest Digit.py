def largest_digit(n):
  
    return max(map(int, str(n)))
n = int(input())
print(largest_digit(n))
