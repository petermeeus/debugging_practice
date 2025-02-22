def swap(a, b):
    a = a - b
    b = a + b
    a = b - a
    return a, b

print(swap(7, 3))  # Expected output: (7, 3)