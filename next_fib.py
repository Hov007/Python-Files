def next_fib(a_list, n):
    # function that giving sum of last two numbers of given list
    def sum_(list_):
        number = list_[len(a_list) - 1] + list_[len(a_list) - 2]
        return number

    needed_len = len(a_list) + n
    while len(a_list) < needed_len:
        new = sum_(a_list)
        a_list.append(new)

    return a_list

a_list = [5, 5, 10, 15, 25, 40, 65]
print(next_fib(a_list, 3))

# Write a function called next_fib. next_fib should take
#have two parameters: a list of integers and a single integer.
#For this description, we'll call the single integer n.
#
#next_fib should modify the list to add the next n pseudo-
#Fibonacci numbers to the end of the sequence. A pseudo-
#Fibonacci number is the sum of the previous two numbers in
#the sequence, but in our case, the previous two numbers may
#not be the original numbers from the Fibonacci sequence.
#
#For example, if the original list given was:
#
# a_list = [5, 5, 10, 15, 25, 40, 65]
#
# Then next_fib(a_list, 3) would return:
#       [5, 5, 10, 15, 25, 40, 65, 105, 170, 275]
#
#All the original numbers in the list are still there, and
#three new ones have been added.
#
#You may assume the list parameter will always have at least
#two numbers.

