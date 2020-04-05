a = int(input("Input positive number a: "))
b = int(input("Input positive number b: " ))
while a > b:
    print("a must be lower than b!")
    a = int(input("Input positive number a: "))
    b = int(input("Input positive number b: "))

# Reversing number function
def reverse(number):
    list1 = []
    res = 0
    for i in str(number):
        list1.append(i)
    list1.reverse()
    res = int("".join(list1))

    return res

# Checking if number isPalindrome function
def isPalindrome(n):
    return n == reverse(n)


# Printing palindrome numbers in given range
for i in range(a, b + 1):
    if isPalindrome(i):
        print(i, end=" ")




