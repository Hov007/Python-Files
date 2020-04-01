def tire_pressure(a):
   # taking last 5 items from list
   b = a[-5:]
   c = []
   count = 0
   sum1 = 0
   avg = 0
   for i in b:
       # putting needed numbers into new list
       if i >= 15 and i <= 55:
           c.append(i)
           count += 1
   n = 6
   while len(c) < 5:
       if a[len(a) - n] >= 15 and a[len(a) - n] <= 55:
           c.append(a[len(a) - n])
           n += 1
       else:
           n = n + 1
   for i in c:
       sum1 += i
   avg = round(sum1 / len(c), 1)
   return avg

# PROBLEM
#Write a function called tire_pressure. tire_pressure
#should have one parameter, a list of integers. The list
#represents a series of tire pressure measurements over the
#past several minutes.
#
#tire_pressure should return the average of the last 5
#measurements that are greater than or equal to 15 and less
#than or equal to 55. Round the result to 1 decimal place
#(you can use round(some_float, 1) to round to 1 decimal
#place).
#
#For example, if the list of measurements was this:
#
# [34, 34, 64, 34, 5, 5, 34, 34, 35, 35, 35, 65, 60, 35, 12, 35]
#
#tire_pressure would return 35.0: the last five measurements
#in range are all 35. You may assume there will be at least
#5 measurements in the proper range.

