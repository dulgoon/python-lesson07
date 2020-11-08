a = int(input("a:"))
b = int(input("b:"))
c = 0
while a <= b:
    a += 1
    if a % 2 == 0:  
        c += a
        print(a)
print("niilber",c)
