def in_range(n, low, high):
    return low <= n <= high

print(in_range(5, 1, 10))  # True
print(in_range(11, 1, 10)) # False
