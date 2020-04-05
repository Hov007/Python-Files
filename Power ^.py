def Power(a, n):
    if n > 0:
        return  a * Power(a, n - 1)
    else:
        return 1

print(Power(2, 1))