height=int(input("Height: "))
thickness=int(input("Thickness: "))

while height % 2 == 0 or thickness % 2 == 0:
    print("You must provide odd numbers")
    height = int(input("Height: "))
    thickness = int(input("Thickness: "))

mid=(height-thickness)//2
# k = mid + thickness
# print(mid, k)
for i in range(height):
    for j in range(height):
        if i in range(mid,mid+thickness) or j in range(mid,mid+thickness):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()