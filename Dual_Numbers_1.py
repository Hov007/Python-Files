number = int(input())
dual_num = True
digit1 = None
digit2 = None
if number >= 100:
   digit1 = number % 10
   digit2 = number // 10 % 10
   if digit1 == digit2:
       digit2 = None
   number //= 100
   while number > 0:
       digit3 = number % 10
       if digit2:
           if digit3 != digit1 and digit3 != digit2:
               dual_num = False
       else:
           digit2 = digit3
       number //= 10
if dual_num:
   print("Dual")
else:
   print("Not Dual")