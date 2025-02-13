def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

print(is_prime(11))  # Expected output: True
print(is_prime(4))   # Expected output: False