def Fibonacci(n):
    if n > 2:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
    else:
        return 1

print(Fibonacci(7))
