year = 3020

if year % 4 != 0:
    print("Normal Year")
elif year % 100 != 0:
    print("Leap Year")
elif year % 400 != 0:
    print("Normal Year")
else:
    print("Leap Year")