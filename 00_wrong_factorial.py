def factorial(n):
    result = 1
    for i in range(1, n+1):
        #print(i)
        result *= i
    return result

print(factorial(5))  # Expected output: 120