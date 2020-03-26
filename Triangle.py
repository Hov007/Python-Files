a = 4
b = 3
c = 5
s = (a+b+c)/2
A = (s*(s-a)*(s-b)*(s-c)) ** 0.5
if A <= 0:
    print("No Triangle")
elif (a ** 2) + (b ** 2) == (c ** 2) or (a ** 2) + (c ** 2) == (b ** 2) or (b ** 2) + (c ** 2) == (a ** 2):
    print("Right Triangle")
elif (a ** 2) + (b ** 2) < (c ** 2) or (a ** 2) + (c ** 2) < (b ** 2) or (b ** 2) + (c ** 2) < (a ** 2):
    print("Obtuse Triangle")
else:
    print("Acute Triangle")